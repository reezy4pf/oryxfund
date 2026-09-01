"""
ORYX FUND — WORM AUDIT TRAIL API ROUTES (backend/app/api/v1/audit.py)
Endpoints for regulatory audit trail inspections and cryptographic hash chain verification.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.core.rbac import require_clearance
from backend.app.services.audit_service import WormAuditService

router = APIRouter(prefix="/audit", tags=["Immutable WORM Audit Trail"])

@router.get("/logs")
async def get_audit_logs(
    limit: int = Query(100, ge=1, le=500),
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_clearance(min_level=4))
):
    """
    Retrieves immutable regulatory WORM audit logs.
    Requires Clearance Level 4 (Fund Manager / CSO) or Level 5 (Compliance / Internal Audit).
    """
    try:
        entries = await WormAuditService.get_audit_trail(db, limit)
        return [
            {
                "audit_event_id": e.audit_event_id,
                "timestamp": e.timestamp.isoformat(),
                "staff_email": e.staff_email,
                "staff_role": e.staff_role,
                "action_type": e.action_type,
                "entity_type": e.entity_type,
                "entity_id": e.entity_id,
                "clearance_level_utilized": e.clearance_level_utilized,
                "state_delta_json": e.state_delta_json,
                "previous_event_hash": e.previous_event_hash,
                "merkle_root_hash": e.merkle_root_hash
            }
            for e in entries
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/verify-chain")
async def verify_cryptographic_audit_chain(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_clearance(min_level=3))
):
    """
    Mathematically verifies the integrity of every hash link in the audit ledger.
    Detects any payload tampering or out-of-sequence mutations.
    """
    try:
        return await WormAuditService.verify_chain_integrity(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
