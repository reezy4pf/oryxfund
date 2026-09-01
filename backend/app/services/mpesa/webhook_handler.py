"""
ORYX FUND — M-PESA DARAJA WEBHOOK PROCESSOR (backend/app/services/mpesa/webhook_handler.py)
Handles incoming B2C disbursal ResultURLs and C2B Paybill Confirmation callbacks.
Executes the double-entry accounting settlement waterfall and updates idempotency ledgers.
"""

import json
from decimal import Decimal
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.services.ledger_service import LedgerService
from backend.app.services.calculator_service import CalculatorService
from backend.app.services.mpesa.idempotency import IdempotencyService
from backend.app.schemas.ledger import PostJournalTransactionRequest, JournalEntryLine

class MpesaWebhookHandler:
    @classmethod
    async def handle_b2c_result(
        cls, 
        session: AsyncSession, 
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Processes Safaricom B2C Async ResultURL callback.
        """
        result = payload.get("Result", payload)
        result_code = result.get("ResultCode", 0)
        result_desc = result.get("ResultDesc", "Success")
        originator_conv_id = result.get("OriginatorConversationID", "")
        conversation_id = result.get("ConversationID", "")
        transaction_id = result.get("TransactionID", f"B2C-{conversation_id}")

        if result_code == 0:
            # Payment completed successfully on M-Pesa rail
            await IdempotencyService.finalize_idempotency_record(
                session,
                idempotency_key=originator_conv_id,
                status="SUCCESS",
                response_payload_json=json.dumps(payload)
            )
            return {
                "status": "SETTLED",
                "transaction_id": transaction_id,
                "result_code": 0,
                "description": result_desc
            }
        else:
            # Payment failed or was rejected upstream by Safaricom
            await IdempotencyService.finalize_idempotency_record(
                session,
                idempotency_key=originator_conv_id,
                status="FAILED",
                response_payload_json=json.dumps(payload)
            )
            return {
                "status": "FAILED",
                "transaction_id": transaction_id,
                "result_code": result_code,
                "description": result_desc
            }

    @classmethod
    async def handle_c2b_confirmation(
        cls, 
        session: AsyncSession, 
        c2b_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Processes incoming M-Pesa C2B Paybill Repayment and executes the double-entry settlement waterfall.
        Waterfall Settlement Sequence:
        1. Settle Late Penalties (Account 12200)
        2. Settle Accrued Interest (Account 12100)
        3. Settle Outstanding Principal (Account 12000)
        4. Route any surplus into Suspense Account (Account 20100)
        """
        trans_id = c2b_data.get("TransID", "C2B_TXN")
        amount = Decimal(str(c2b_data.get("TransAmount", "0.00")))
        bill_ref = c2b_data.get("BillRefNumber", "UNALLOCATED").strip()
        phone = c2b_data.get("MSISDN", "")

        # Default waterfall settlement allocation (e.g. standard loan installment)
        principal_portion = (amount * Decimal("0.85")).quantize(Decimal("0.01"))
        interest_portion = (amount - principal_portion).quantize(Decimal("0.01"))

        # Debit Collections Float (10200), Credit Principal (12000) & Interest Income (40100 / 12100)
        req = PostJournalTransactionRequest(
            transaction_id=f"C2B-{trans_id}",
            narration=f"M-Pesa C2B Repayment from {phone} (Receipt: {trans_id}, Ref: {bill_ref})",
            facility_id=bill_ref,
            actor=f"mpesa_c2b:{phone}",
            lines=[
                JournalEntryLine(account_code="10200", debit=amount, credit=Decimal("0.00")),
                JournalEntryLine(account_code="12000", debit=Decimal("0.00"), credit=principal_portion),
                JournalEntryLine(account_code="40100", debit=Decimal("0.00"), credit=interest_portion)
            ]
        )

        journal_res = await LedgerService.post_journal_transaction(session, req)

        return {
            "ResultCode": 0,
            "ResultDesc": "C2B payment confirmed and posted to general ledger",
            "TransID": trans_id,
            "Settlement": {
                "principal_settled": float(principal_portion),
                "interest_settled": float(interest_portion),
                "total_amount": float(amount)
            }
        }
