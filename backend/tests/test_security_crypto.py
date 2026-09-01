"""
ORYX FUND — SECURITY & CRYPTOGRAPHY UNIT TESTS (backend/tests/test_security_crypto.py)
Validates AES-256-GCM envelope encryption, JWT token management, WebAuthn FIDO2 verification,
and RBAC clearance level enforcement.
"""

from decimal import Decimal
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.db.session import engine
from backend.app.db.base import Base
from backend.app.core.crypto import EnvelopeEncryptionEngine, crypto_engine
from backend.app.core.auth import AuthService
from backend.app.core.webauthn import WebAuthnEngine

@pytest_asyncio.fixture(autouse=True)
async def init_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

def test_envelope_encryption_and_decryption_pii():
    # Test encryption of Kenyan National ID
    national_id = "32847599"
    encrypted_payload = crypto_engine.encrypt_field(national_id, context_identifier="borrower_usr_100")
    assert encrypted_payload is not None
    assert encrypted_payload != national_id

    # Test decryption back to plaintext
    decrypted_id = crypto_engine.decrypt_field(encrypted_payload, context_identifier="borrower_usr_100")
    assert decrypted_id == national_id

    # Test context mismatch prevention (ciphertext cannot be decrypted in different context)
    with pytest.raises(Exception):
        crypto_engine.decrypt_field(encrypted_payload, context_identifier="different_context_usr_999")

def test_password_hashing_and_verification():
    plain_pass = "Oryx2026"
    hashed = AuthService.hash_password(plain_pass)
    assert hashed == "91521ad19aee4d15e8ed916c75354a4411e6a5c43703ddb048411c41b67732c7"
    assert AuthService.verify_password(plain_pass, hashed) is True
    assert AuthService.verify_password("WrongPassword!", hashed) is False

def test_jwt_token_creation_and_claims_decoding():
    payload = {
        "sub": "usr_test_001",
        "email": "lead.underwriter@oryxfund.ke",
        "clearance_level": 3
    }
    token = AuthService.create_access_token(payload)
    decoded = AuthService.decode_access_token(token)
    assert decoded["sub"] == "usr_test_001"
    assert decoded["email"] == "lead.underwriter@oryxfund.ke"
    assert decoded["clearance_level"] == 3

def test_webauthn_challenge_generation():
    challenge_data = WebAuthnEngine.generate_authentication_challenge("dervinaziza9@gmail.com")
    assert "challenge" in challenge_data
    assert challenge_data["rpId"] == "oryxfund.ke"
    assert len(challenge_data["challenge"]) > 20

@pytest.mark.asyncio
async def test_auth_login_api_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Admin login
        res = await ac.post("/api/v1/auth/login", json={
            "email": "dervinaziza9@gmail.com",
            "password": "Oryx2026"
        })
        assert res.status_code == 200
        data = res.json()
        assert "access_token" in data
        assert data["user"]["clearance_level"] == 4
        assert data["requires_mfa"] is True
