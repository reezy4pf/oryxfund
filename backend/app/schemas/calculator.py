"""
ORYX FUND — CALCULATOR SCHEMAS (backend/app/schemas/calculator.py)
Pydantic validation schemas for loan amortization, KRA excise duty, and CBK provisioning endpoints.
"""

from decimal import Decimal
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field

class AmortizationRequest(BaseModel):
    principal: Decimal = Field(..., gt=0, description="Gross loan principal in KES")
    annual_rate_percent: Decimal = Field(default=Decimal("14.00"), gt=0, description="Annual interest rate percentage")
    tenure_months: int = Field(default=12, gt=0, le=60, description="Tenure in months")

class InstallmentItem(BaseModel):
    installment_number: int
    due_date: str
    beginning_balance: Decimal
    monthly_payment: Decimal
    principal_payment: Decimal
    interest_payment: Decimal
    ending_balance: Decimal

class AmortizationResponse(BaseModel):
    principal: Decimal
    annual_rate_percent: Decimal
    tenure_months: int
    monthly_installment: Decimal
    total_repayment: Decimal
    total_interest: Decimal
    schedule: List[InstallmentItem]

class ExciseDutyRequest(BaseModel):
    principal: Decimal = Field(..., gt=0, description="Gross loan principal in KES")
    fee_rate_percent: Decimal = Field(default=Decimal("2.00"), gt=0, le=10, description="Processing fee percentage")

class ExciseDutyResponse(BaseModel):
    principal: Decimal
    fee_rate_percent: Decimal
    net_processing_fee: Decimal
    excise_duty_payable_kra: Decimal
    gross_fee_deduction: Decimal
    net_disbursement: Decimal

class CBKProvisioningRequest(BaseModel):
    days_past_due: int = Field(default=0, ge=0, description="Days Past Due (DPD)")
    outstanding_balance: Decimal = Field(..., ge=0, description="Outstanding loan balance in KES")

class CBKProvisioningResponse(BaseModel):
    days_past_due: int
    outstanding_balance: Decimal
    classification: str
    ifrs9_stage: str
    provision_rate_percent: Decimal
    provision_amount: Decimal
    risk_tier: str
