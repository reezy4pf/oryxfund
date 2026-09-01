"""
ORYX FUND — CRB PIPELINE UNIT TESTS (backend/tests/test_crb_pipeline.py)
Validates real-time credit report fetching, credit scoring categorization,
and monthly regulatory submission data generation per CRB Regulations 2020.
"""

from decimal import Decimal
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.db.session import engine
from backend.app.db.base import Base
from backend.app.services.crb.crb_client import CRBClient

@pytest_asyncio.fixture(autouse=True)
async def init_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

@pytest.mark.asyncio
async def test_crb_credit_scoring_prime():
    client = CRBClient(provider="TransUnion")
    report = await client.fetch_credit_report(
        national_id="32847599",
        phone_number="+254712345678",
        stated_monthly_income=Decimal("180000.00")
    )
    assert report["credit_score"] == 760
    assert report["score_band"] == "Prime (Tier 1)"
    assert report["active_defaults_count"] == 0
    assert report["recommendation"] == "APPROVE"

@pytest.mark.asyncio
async def test_crb_credit_scoring_delinquent():
    client = CRBClient(provider="Metropol")
    report = await client.fetch_credit_report(
        national_id="32847590",
        phone_number="+254712345678",
        stated_monthly_income=Decimal("80000.00")
    )
    assert report["credit_score"] == 480
    assert report["score_band"] == "Subprime / High Risk"
    assert report["active_defaults_count"] > 0
    assert report["recommendation"] == "DECLINE_DELINQUENT"

@pytest.mark.asyncio
async def test_crb_score_api_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.post("/api/v1/crb/score", json={
            "national_id": "28394857",
            "phone_number": "0711223344",
            "stated_monthly_income": 150000.00,
            "provider": "Creditinfo"
        })
        assert res.status_code == 200
        data = res.json()
        assert data["bureau_provider"] == "Creditinfo"
        assert "credit_score" in data

@pytest.mark.asyncio
async def test_crb_monthly_submission_api():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/api/v1/crb/monthly-submission")
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "VALIDATED_CRB_REGULATIONS_2020"
        assert isinstance(data["records"], list)
