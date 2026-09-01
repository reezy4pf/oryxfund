"""
ORYX FUND — M-PESA DARAJA 2.0 API ROUTES (backend/app/api/v1/mpesa.py)
Endpoints for B2C bulk disbursal, C2B validation/confirmation, and Lipa Na M-Pesa STK Push.
"""

from decimal import Decimal
from typing import Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Body, Header
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.core.rbac import require_clearance_level
from backend.app.services.mpesa.daraja_client import DarajaClient
from backend.app.services.mpesa.idempotency import IdempotencyService
from backend.app.services.mpesa.webhook_handler import MpesaWebhookHandler

router = APIRouter(prefix="/mpesa", tags=["Safaricom M-Pesa Daraja 2.0"])
daraja_client = DarajaClient()

class B2CDisbursementRequest(BaseModel):
    loan_id: str = Field(..., description="Unique Loan ID (e.g. ACC-LOAN-2026-00001)")
    borrower_phone: str = Field(..., description="Kenyan MSISDN in 2547... or 07... format")
    amount: Decimal = Field(..., gt=0, description="Net disbursement principal in KES")
    remarks: Optional[str] = Field(default="Oryx Fund Working Capital Disbursal")

class STKPushRequest(BaseModel):
    phone_number: str = Field(..., description="Kenyan phone number")
    amount: Decimal = Field(..., gt=0, description="Repayment amount in KES")
    account_reference: str = Field(..., description="Loan Reference Number")
    transaction_desc: Optional[str] = Field(default="Oryx Fund Loan Repayment")

@router.post("/b2c/disburse")
async def disburse_loan_b2c(
    req: B2CDisbursementRequest,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key"),
    current_user: Dict[str, Any] = Depends(require_clearance_level(4)),
    db: AsyncSession = Depends(get_db)
):
    """
    Executes an automated, idempotent B2C loan disbursement to the borrower's M-Pesa account.
    Requires Clearance Level 4 (Fund Manager / Lead Underwriter).
    """
    # 1. Derive or validate deterministic idempotency key
    key = idempotency_key or IdempotencyService.generate_disbursement_key(req.loan_id)

    # 2. Check for duplicate processing
    existing_record = await IdempotencyService.get_idempotency_status(db, key)
    if existing_record:
        if existing_record.status == "SUCCESS":
            return {
                "status": "ALREADY_COMPLETED",
                "idempotency_key": key,
                "message": "Transaction previously processed and confirmed."
            }
        elif existing_record.status == "PROCESSING":
            raise HTTPException(status_code=425, detail="Disbursement transaction currently in progress.")

    # 3. Create idempotency lock
    await IdempotencyService.create_idempotency_record(db, key, status="PROCESSING")

    # 4. Dispatch to Safaricom Daraja B2C Gateway
    try:
        daraja_response = await daraja_client.initiate_b2c_disbursement(
            borrower_phone=req.borrower_phone,
            amount=req.amount,
            loan_id=req.loan_id,
            idempotency_key=key,
            remarks=req.remarks
        )

        return {
            "status": "ACCEPTED",
            "idempotency_key": key,
            "loan_id": req.loan_id,
            "daraja_response": daraja_response
        }
    except Exception as e:
        await IdempotencyService.finalize_idempotency_record(db, key, status="FAILED")
        raise HTTPException(status_code=502, detail=f"Payment gateway communication error: {str(e)}")

@router.post("/b2c/result")
async def b2c_result_callback(
    payload: Dict[str, Any] = Body(...),
    db: AsyncSession = Depends(get_db)
):
    """Safaricom Daraja B2C Async Webhook Receiver (ResultURL)."""
    return await MpesaWebhookHandler.handle_b2c_result(db, payload)

@router.post("/c2b/validation")
async def c2b_validation_callback(payload: Dict[str, Any] = Body(...)):
    """M-Pesa C2B Paybill Validation webhook."""
    return {"ResultCode": 0, "ResultDesc": "Accepted"}

@router.post("/c2b/confirmation")
async def c2b_confirmation_callback(
    payload: Dict[str, Any] = Body(...),
    db: AsyncSession = Depends(get_db)
):
    """M-Pesa C2B Paybill Confirmation webhook."""
    return await MpesaWebhookHandler.handle_c2b_confirmation(db, payload)

@router.post("/stk/push")
async def trigger_stk_push(req: STKPushRequest):
    """Triggers an M-Pesa STK Push prompt on borrower's mobile phone."""
    return await daraja_client.initiate_stk_push(
        phone_number=req.phone_number,
        amount=req.amount,
        account_reference=req.account_reference,
        transaction_desc=req.transaction_desc
    )
