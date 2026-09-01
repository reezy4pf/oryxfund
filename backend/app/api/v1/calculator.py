"""
ORYX FUND — CALCULATOR API ROUTES (backend/app/api/v1/calculator.py)
Endpoints for loan amortization schedules, statutory 20% KRA excise duty, and CBK provisioning.
"""

from decimal import Decimal
from fastapi import APIRouter, HTTPException
from backend.app.schemas.calculator import (
    AmortizationRequest, AmortizationResponse, InstallmentItem,
    ExciseDutyRequest, ExciseDutyResponse,
    CBKProvisioningRequest, CBKProvisioningResponse
)
from backend.app.services.calculator_service import CalculatorService

router = APIRouter(prefix="/calculator", tags=["Financial Calculator & Risk Engine"])

@router.post("/amortization", response_model=AmortizationResponse)
async def calculate_amortization(req: AmortizationRequest):
    """Generates complete periodic reducing-balance loan amortization schedule."""
    try:
        monthly_pmt = CalculatorService.calculate_monthly_installment(
            req.principal, req.annual_rate_percent, req.tenure_months
        )
        total_repay = (monthly_pmt * req.tenure_months).quantize(Decimal("0.01"))
        total_interest = (total_repay - req.principal).quantize(Decimal("0.01"))
        raw_schedule = CalculatorService.generate_amortization_schedule(
            req.principal, req.annual_rate_percent, req.tenure_months
        )

        schedule_items = [InstallmentItem(**item) for item in raw_schedule]

        return AmortizationResponse(
            principal=req.principal,
            annual_rate_percent=req.annual_rate_percent,
            tenure_months=req.tenure_months,
            monthly_installment=monthly_pmt,
            total_repayment=total_repay,
            total_interest=total_interest,
            schedule=schedule_items
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/excise-duty", response_model=ExciseDutyResponse)
async def calculate_excise_duty(req: ExciseDutyRequest):
    """Calculates statutory Kenyan 20% KRA Excise Duty on loan processing fees."""
    try:
        result = CalculatorService.calculate_origination_fee_with_excise(
            req.principal, req.fee_rate_percent
        )
        return ExciseDutyResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/provisioning", response_model=CBKProvisioningResponse)
async def calculate_provisioning(req: CBKProvisioningRequest):
    """Classifies facility under CBK Prudential Guidelines and IFRS 9 loan loss staging."""
    try:
        res = CalculatorService.classify_cbk_provisioning(req.days_past_due, req.outstanding_balance)
        return CBKProvisioningResponse(
            days_past_due=req.days_past_due,
            outstanding_balance=req.outstanding_balance,
            **res
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
