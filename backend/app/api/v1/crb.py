"""
ORYX FUND — CRB API ROUTES (backend/app/api/v1/crb.py)
Endpoints for borrower credit bureau queries and monthly regulatory submission generation.
"""

from decimal import Decimal
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.services.crb.crb_client import CRBClient
from backend.app.services.crb.submission import CRBSubmissionService

router = APIRouter(prefix="/crb", tags=["Credit Reference Bureau (CRB) Pipeline"])

class CreditScoreRequest(BaseModel):
    national_id: str = Field(..., description="Kenyan National ID Number")
    phone_number: str = Field(..., description="Borrower primary phone number")
    stated_monthly_income: Decimal = Field(default=Decimal("150000.00"), gt=0)
    provider: Optional[str] = Field(default="TransUnion")

@router.post("/score")
async def pull_credit_report(req: CreditScoreRequest):
    """
    Pulls a real-time credit score and delinquency report from licensed Kenyan CRBs.
    """
    try:
        client = CRBClient(provider=req.provider)
        return await client.fetch_credit_report(
            national_id=req.national_id,
            phone_number=req.phone_number,
            stated_monthly_income=req.stated_monthly_income
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/monthly-submission")
async def get_monthly_submission(db: AsyncSession = Depends(get_db)):
    """
    Generates the standardized monthly credit data submission file per CRB Regulations 2020.
    """
    try:
        data = await CRBSubmissionService.generate_monthly_submission_data(db)
        return {
            "record_count": len(data),
            "status": "VALIDATED_CRB_REGULATIONS_2020",
            "records": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
