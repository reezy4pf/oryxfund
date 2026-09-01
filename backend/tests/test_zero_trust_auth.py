"""
ORYX FUND — ZERO-TRUST SECURITY & IAM AUTOMATED TEST BATTERY (backend/tests/test_zero_trust_auth.py)
Validates strict zero-trust authentication, token validation, unauthenticated rejection (401),
tamper detection, and RBAC clearance level enforcement.
"""

import pytest
from httpx import AsyncClient, ASGITransport
from datetime import datetime, timezone, timedelta
from backend.app.main import app
from backend.app.core.auth import AuthService
from backend.app.core.config import settings

@pytest.mark.asyncio
async def test_unauthenticated_requests_strictly_return_401():
    """Verify that any request missing a Bearer token is strictly rejected with HTTP 401."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Protected Audit endpoint
        res_audit = await ac.get("/api/v1/audit/logs")
        assert res_audit.status_code == 401
        assert "Authentication required" in res_audit.json()["detail"]

        # Protected Audit chain verification endpoint
        res_chain = await ac.get("/api/v1/audit/verify-chain")
        assert res_chain.status_code == 401

        # Protected Ledger journal endpoint
        res_journal = await ac.post("/api/v1/ledger/journal", json={
            "transaction_id": "TXN-TEST-001",
            "narration": "Test transaction",
            "facility_id": "ACC-LOAN-001",
            "lines": [
                {"account_code": "12000", "debit": 1000.0, "credit": 0.0},
                {"account_code": "10100", "debit": 0.0, "credit": 1000.0}
            ]
        })
        assert res_journal.status_code == 401

        # Protected M-Pesa B2C Disbursal endpoint
        res_mpesa = await ac.post("/api/v1/mpesa/b2c/disburse", json={
            "borrower_phone": "254712345678",
            "amount": 5000.0,
            "loan_id": "ACC-LOAN-001"
        })
        assert res_mpesa.status_code == 401

@pytest.mark.asyncio
async def test_authenticated_admin_request_succeeds():
    """Verify that a valid authenticated Level 4 Admin session successfully accesses protected routes."""
    admin_payload = {
        "sub": "usr_admin_001",
        "name": "Dervin Aziza",
        "email": settings.ADMIN_DEFAULT_EMAIL,
        "role": "Fund Manager / Lead Underwriter",
        "clearance_level": 4
    }
    token = AuthService.create_access_token(admin_payload)
    headers = {"Authorization": f"Bearer {token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        res = await ac.get("/api/v1/audit/logs", headers=headers)
        assert res.status_code == 200
        assert isinstance(res.json(), list)

@pytest.mark.asyncio
async def test_tampered_jwt_token_rejected_with_401():
    """Verify that an altered/forged JWT signature is strictly rejected with HTTP 401."""
    admin_payload = {
        "sub": "usr_admin_001",
        "name": "Attacker",
        "email": "hacker@evil.com",
        "role": "Admin",
        "clearance_level": 5
    }
    # Forge a token using a false secret
    fake_token = AuthService.create_access_token(admin_payload)
    tampered_token = fake_token[:-5] + "XXXXX"

    headers = {"Authorization": f"Bearer {tampered_token}"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        res = await ac.get("/api/v1/audit/logs", headers=headers)
        assert res.status_code == 401

@pytest.mark.asyncio
async def test_rbac_clearance_level_guard():
    """Verify that a Level 1 / Level 2 user cannot access Level 3+ Admin endpoints."""
    officer_payload = {
        "sub": "usr_officer_002",
        "name": "Junior Officer",
        "email": "officer@oryxfund.ke",
        "role": "Junior Officer",
        "clearance_level": 2 # Clearance 2 < Required Clearance 3 for journal posting
    }
    token = AuthService.create_access_token(officer_payload)
    headers = {"Authorization": f"Bearer {token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Posting to Ledger requires Clearance Level 3+
        res = await ac.post("/api/v1/ledger/journal", headers=headers, json={
            "transaction_id": "TXN-TEST-002",
            "narration": "Unauthorized journal post",
            "facility_id": "ACC-LOAN-001",
            "lines": [
                {"account_code": "12000", "debit": 1000.0, "credit": 0.0},
                {"account_code": "10100", "debit": 0.0, "credit": 1000.0}
            ]
        })
        assert res.status_code == 403
        assert "Insufficient clearance" in res.json()["detail"]
