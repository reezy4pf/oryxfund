"""
ORYX FUND — TELEMETRY & OBSERVABILITY API ROUTES (backend/app/api/v1/telemetry.py)
Endpoints for Prometheus metric scrapes and real-time FinTech risk telemetry.
"""

from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.core.telemetry import TelemetryEngine

router = APIRouter(prefix="/telemetry", tags=["Observability & Telemetry"])

@router.get("/risk")
async def get_realtime_portfolio_risk_telemetry(db: AsyncSession = Depends(get_db)):
    """
    Returns real-time balance sheet risk telemetry:
    PAR 30/60/90, NPL Ratio, Collection Efficiency, and CBK 5-tier provisioning breakdown.
    """
    return await TelemetryEngine.get_realtime_risk_metrics(db)
