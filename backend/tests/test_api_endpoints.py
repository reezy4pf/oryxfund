"""
ORYX FUND — API ENDPOINT INTEGRATION TESTS (backend/tests/test_api_endpoints.py)
Validates FastAPI endpoints for health, calculator math, and double-entry ledger transactions via async HTTP client.
"""

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.db.session import engine
from backend.app.db.base import Base

@pytest_asyncio.fixture(autouse=True)
async def init_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

@pytest.mark.asyncio
async def test_health_check_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ONLINE"
    assert data["cbk_dcp_compliance"] == "ACTIVE"
    assert data["ledger_engine"] == "DOUBLE_ENTRY_ACID"

@pytest.mark.asyncio
async def test_calculator_amortization_api():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/calculator/amortization", json={
            "principal": 50000.00,
            "annual_rate_percent": 18.00,
            "tenure_months": 24
        })
    assert response.status_code == 200
    data = response.json()
    assert float(data["monthly_installment"]) == 2496.21
    assert len(data["schedule"]) == 24

@pytest.mark.asyncio
async def test_calculator_excise_duty_api():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/calculator/excise-duty", json={
            "principal": 50000.00,
            "fee_rate_percent": 3.00
        })
    assert response.status_code == 200
    data = response.json()
    assert float(data["net_processing_fee"]) == 1500.00
    assert float(data["excise_duty_payable_kra"]) == 300.00
    assert float(data["net_disbursement"]) == 48200.00

@pytest.mark.asyncio
async def test_calculator_provisioning_api():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/calculator/provisioning", json={
            "days_past_due": 45,
            "outstanding_balance": 100000.00
        })
    assert response.status_code == 200
    data = response.json()
    assert data["classification"] == "Watch (Underperforming)"
    assert data["ifrs9_stage"] == "Stage 2"
    assert float(data["provision_amount"]) == 3000.00

@pytest.mark.asyncio
async def test_post_journal_and_trial_balance_api():
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
        # 1. Post Disbursal Journal Transaction
        post_res = await ac.post("/api/v1/ledger/journal", headers=headers, json={
            "transaction_id": "TXN-API-001",
            "narration": "API Disbursal Test",
            "facility_id": "LND-API-001",
            "lines": [
                {"account_code": "12000", "debit": 50000.00, "credit": 0.00},
                {"account_code": "10100", "debit": 0.00, "credit": 48200.00},
                {"account_code": "40200", "debit": 0.00, "credit": 1500.00},
                {"account_code": "20200", "debit": 0.00, "credit": 300.00}
            ]
        })
        assert post_res.status_code == 200
        post_data = post_res.json()
        assert post_data["success"] is True
        assert post_data["transaction_id"] == "TXN-API-001"

        # 2. Query Trial Balance API
        tb_res = await ac.get("/api/v1/ledger/trial-balance", headers=headers)
        assert tb_res.status_code == 200
        tb_data = tb_res.json()
        assert tb_data["is_balanced"] is True
        assert float(tb_data["total_debit"]) >= 50000.00
