"""
ORYX FUND — OBSERVABILITY & TELEMETRY UNIT TESTS (backend/tests/test_observability.py)
Validates Prometheus metric exposition, Sentry PII scrubbing, and real-time FinTech risk telemetry.
"""

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from backend.app.db.session import engine
from backend.app.db.base import Base
from backend.app.core.telemetry import TelemetryEngine

@pytest_asyncio.fixture(autouse=True)
async def init_test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

def test_sentry_pii_sanitization():
    raw_payload = {
        "applicant_name": "John Kamau",
        "national_id": "32847599",
        "kra_pin": "A009182736Z",
        "borrower_phone": "254712345678",
        "requested_amount": 50000.00
    }
    sanitized = TelemetryEngine.sanitize_pii(raw_payload)
    assert sanitized["national_id"] == "[REDACTED_PII]"
    assert sanitized["kra_pin"] == "[REDACTED_PII]"
    assert "2547" in sanitized["borrower_phone"] and "****" in sanitized["borrower_phone"]
    assert sanitized["requested_amount"] == 50000.00

@pytest.mark.asyncio
async def test_prometheus_metrics_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/metrics")
        assert res.status_code == 200
        text = res.text
        assert "oryx_http_requests_total" in text
        assert "oryx_b2c_availability_ratio" in text
        assert "oryx_par_30_percent" in text

@pytest.mark.asyncio
async def test_realtime_risk_telemetry_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/api/v1/telemetry/risk")
        assert res.status_code == 200
        data = res.json()
        assert "portfolio_at_risk_par30_percent" in data
        assert "mpesa_b2c_engine_availability_percent" in data
        assert data["regulatory_status"] == "CBK_DCP_COMPLIANT_GREEN"
