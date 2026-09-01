"""
ORYX FUND — M-PESA DARAJA & IDEMPOTENCY UNIT TESTS (backend/tests/test_mpesa_daraja.py)
Validates STK Push password generation, deterministic UUIDv5 idempotency keys,
B2C disbursals, and C2B double-entry settlement waterfall.
"""

from decimal import Decimal
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.db.session import engine
from backend.app.db.base import Base
from backend.app.services.mpesa.daraja_client import DarajaClient
from backend.app.services.mpesa.idempotency import IdempotencyService
from backend.app.services.mpesa.webhook_handler import MpesaWebhookHandler

@pytest_asyncio.fixture(autouse=True)
async def init_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

def test_stk_password_generation():
    client = DarajaClient(c2b_shortcode="174379", passkey="testpasskey")
    pwd_info = client.generate_stk_password(timestamp_str="20260901120000")
    assert pwd_info["timestamp"] == "20260901120000"
    assert len(pwd_info["password"]) > 20

def test_deterministic_idempotency_key_derivation():
    key1 = IdempotencyService.generate_disbursement_key("ACC-LOAN-2026-00001", tranche_index=1)
    key2 = IdempotencyService.generate_disbursement_key("ACC-LOAN-2026-00001", tranche_index=1)
    key3 = IdempotencyService.generate_disbursement_key("ACC-LOAN-2026-00002", tranche_index=1)
    
    # Must be 100% deterministic and match across identical calls
    assert key1 == key2
    assert key1 != key3

@pytest.mark.asyncio
async def test_mpesa_b2c_disbursement_api():
    from backend.app.core.auth import AuthService
    token = AuthService.create_access_token({
        "sub": "usr_admin_001",
        "name": "Dervin Aziza",
        "email": "dervinaziza9@gmail.com",
        "role": "Fund Manager",
        "clearance_level": 4
    })
    headers = {"Authorization": f"Bearer {token}"}

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        import uuid
        loan_id = f"ACC-LOAN-2026-TEST-{uuid.uuid4().hex[:8]}"
        res = await ac.post("/api/v1/mpesa/b2c/disburse", headers=headers, json={
            "loan_id": loan_id,
            "borrower_phone": "254712345678",
            "amount": 25000.00,
            "remarks": "Disbursal test"
        })
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "ACCEPTED"
        assert "idempotency_key" in data

        # Test duplicate submission with identical idempotency key
        idem_key = data["idempotency_key"]
        dup_headers = {"Authorization": f"Bearer {token}", "Idempotency-Key": idem_key}
        dup_res = await ac.post(
            "/api/v1/mpesa/b2c/disburse",
            json={
                "loan_id": loan_id,
                "borrower_phone": "254712345678",
                "amount": 25000.00
            },
            headers=dup_headers
        )
        assert dup_res.status_code == 425 # 425 Too Early (in progress)

@pytest.mark.asyncio
async def test_mpesa_c2b_confirmation_settlement_waterfall():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.post("/api/v1/mpesa/c2b/confirmation", json={
            "TransactionType": "Pay Bill",
            "TransID": "QK91827364",
            "TransTime": "20260901140000",
            "TransAmount": "23750.00",
            "BusinessShortCode": "600000",
            "BillRefNumber": "ACC-LOAN-2026-00001",
            "MSISDN": "254712345678",
            "FirstName": "Alex"
        })
        assert res.status_code == 200
        data = res.json()
        assert data["ResultCode"] == 0
        assert data["Settlement"]["total_amount"] == 23750.00
        assert data["Settlement"]["principal_settled"] > 0
        assert data["Settlement"]["interest_settled"] > 0

@pytest.mark.asyncio
async def test_mpesa_stk_push_api():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.post("/api/v1/mpesa/stk/push", json={
            "phone_number": "0712345678",
            "amount": 5000.00,
            "account_reference": "ACC-LOAN-2026-00001"
        })
        assert res.status_code == 200
        data = res.json()
        assert data["ResponseCode"] == "0"
