"""
ORYX FUND — LEDGER API ROUTES (backend/app/api/v1/ledger.py)
Endpoints for posting double-entry transactions, querying trial balances, and inspecting general ledger entries.
"""

from typing import List, Optional, Dict
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.core.rbac import require_clearance_level
from backend.app.schemas.ledger import (
    PostJournalTransactionRequest, JournalTransactionResponse, TrialBalanceResponse
)
from backend.app.services.ledger_service import LedgerService

router = APIRouter(prefix="/ledger", tags=["Double-Entry Accounting Ledger"])

@router.post("/journal", response_model=JournalTransactionResponse)
async def post_journal_entry(
    req: PostJournalTransactionRequest,
    current_user: Dict = Depends(require_clearance_level(3)),
    db: AsyncSession = Depends(get_db)
):
    """
    Posts an atomic double-entry journal transaction.
    Enforces the core accounting invariant: Total Debits == Total Credits.
    Requires Clearance Level 3 (Senior Accountant / Underwriter).
    """
    try:
        res = await LedgerService.post_journal_transaction(db, req)
        return JournalTransactionResponse(**res)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trial-balance", response_model=TrialBalanceResponse)
async def get_trial_balance(
    current_user: Dict = Depends(require_clearance_level(2)),
    db: AsyncSession = Depends(get_db)
):
    """
    Generates the real-time statutory Trial Balance across all Chart of Accounts.
    Requires Clearance Level 2 (Staff / Auditor).
    """
    try:
        return await LedgerService.get_trial_balance(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/entries")
async def get_ledger_entries(
    facility_id: Optional[str] = Query(None, description="Filter by Loan Facility ID"),
    account_code: Optional[str] = Query(None, description="Filter by Account Code"),
    limit: int = Query(100, ge=1, le=500),
    db: AsyncSession = Depends(get_db)
):
    """Retrieves recent general ledger journal entries."""
    try:
        entries = await LedgerService.get_ledger_entries(db, facility_id, account_code, limit)
        return [
            {
                "entry_id": e.entry_id,
                "transaction_id": e.transaction_id,
                "account_code": e.account_code,
                "facility_id": e.facility_id,
                "debit_amount": float(e.debit_amount),
                "credit_amount": float(e.credit_amount),
                "currency": e.currency,
                "booking_date": e.booking_date.isoformat(),
                "value_timestamp": e.value_timestamp.isoformat(),
                "narration": e.narration,
                "actor": e.actor
            }
            for e in entries
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
