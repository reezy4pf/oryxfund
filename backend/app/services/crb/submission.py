"""
ORYX FUND — CRB STATUTORY MONTHLY SUBMISSION ENGINE (backend/app/services/crb/submission.py)
Formats loan facility performance data into standardized monthly regulatory transmission files
per Credit Reference Bureau Regulations 2020.
"""

from decimal import Decimal
from datetime import date
from typing import List, Dict, Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.ledger import LoanFacility

class CRBSubmissionService:
    @classmethod
    async def generate_monthly_submission_data(
        cls, 
        session: AsyncSession, 
        reporting_period_end: date = date.today()
    ) -> List[Dict[str, Any]]:
        """
        Extracts active and closed facilities, categorizes repayment statuses,
        and generates the standard bureau transmission schema.
        """
        stmt = select(LoanFacility)
        result = await session.execute(stmt)
        facilities = result.scalars().all()

        records = []
        for fac in facilities:
            # Map DPD to CRB Classification Code
            if fac.days_past_due <= 30:
                acc_status = "00 (Performing)"
            elif fac.days_past_due <= 60:
                acc_status = "30 (Watch)"
            elif fac.days_past_due <= 90:
                acc_status = "60 (Substandard)"
            elif fac.days_past_due <= 180:
                acc_status = "90 (Doubtful)"
            else:
                acc_status = "180 (Loss / Write-off)"

            records.append({
                "facility_id": fac.loan_id,
                "borrower_name": fac.customer_name,
                "sanctioned_amount": float(fac.sanctioned_principal),
                "outstanding_balance": float(fac.outstanding_balance),
                "monthly_installment": float(fac.monthly_installment),
                "days_past_due": fac.days_past_due,
                "account_status_code": acc_status,
                "disbursed_date": fac.disbursed_date.isoformat(),
                "reporting_date": reporting_period_end.isoformat(),
                "currency": "KES"
            })

        return records
