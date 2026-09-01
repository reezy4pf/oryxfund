"""
ORYX FUND — FINANCIAL CALCULATION & RISK ENGINE (backend/app/services/calculator_service.py)
High-precision Decimal arithmetic implementation of reducing-balance loan amortization,
statutory Kenyan KRA 20% excise duty on fees, CBK Prudential Guidelines / IFRS 9 staging,
Portfolio at Risk (PAR), and Collection Efficiency.
"""

from decimal import Decimal, ROUND_HALF_UP
from datetime import date, timedelta
from typing import List, Dict, Any

class CalculatorService:
    STATUTORY_EXCISE_DUTY_RATE = Decimal("0.20")  # 20% KRA Excise Duty on Processing Fees
    DEFAULT_FEE_RATE = Decimal("0.02")           # 2.0% Processing Fee

    @classmethod
    def calculate_monthly_installment(
        cls, 
        principal: Decimal, 
        annual_rate_percent: Decimal, 
        tenure_months: int
    ) -> Decimal:
        """
        Computes the exact monthly payment using the standard reducing-balance EMI formula:
        PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
        """
        if principal <= Decimal("0.00") or tenure_months <= 0:
            raise ValueError("Principal and tenure must be strictly positive.")

        monthly_rate = (annual_rate_percent / Decimal("100") / Decimal("12")).quantize(Decimal("0.00000001"))

        if monthly_rate == Decimal("0.00"):
            return (principal / Decimal(tenure_months)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        # Factor = (1 + r)^n
        compounded_factor = (Decimal("1.00") + monthly_rate) ** tenure_months
        numerator = principal * (monthly_rate * compounded_factor)
        denominator = compounded_factor - Decimal("1.00")

        pmt = numerator / denominator
        return pmt.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @classmethod
    def calculate_origination_fee_with_excise(
        cls, 
        principal: Decimal, 
        fee_rate_percent: Decimal = Decimal("2.00")
    ) -> Dict[str, Decimal]:
        """
        Calculates statutory Kenyan KRA 20% Excise Duty on processing and facility appraisal fees.
        Net Processing Fee = Principal * Fee Rate
        Excise Duty (KRA) = Net Fee * 20%
        Gross Fee Deduction = Net Fee + Excise Duty
        Net Disbursal Amount = Principal - Gross Fee Deduction
        """
        net_fee = (principal * (fee_rate_percent / Decimal("100"))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        excise_duty = (net_fee * cls.STATUTORY_EXCISE_DUTY_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        gross_fee = (net_fee + excise_duty).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        net_disbursement = (principal - gross_fee).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return {
            "principal": principal,
            "fee_rate_percent": fee_rate_percent,
            "net_processing_fee": net_fee,
            "excise_duty_payable_kra": excise_duty,
            "gross_fee_deduction": gross_fee,
            "net_disbursement": net_disbursement
        }

    @classmethod
    def generate_amortization_schedule(
        cls, 
        principal: Decimal, 
        annual_rate_percent: Decimal, 
        tenure_months: int,
        start_date: date = date.today()
    ) -> List[Dict[str, Any]]:
        """
        Generates a complete periodic reducing-balance amortization schedule.
        """
        schedule = []
        balance = principal
        monthly_payment = cls.calculate_monthly_installment(principal, annual_rate_percent, tenure_months)
        monthly_rate = (annual_rate_percent / Decimal("100") / Decimal("12")).quantize(Decimal("0.00000001"))

        for month in range(1, tenure_months + 1):
            interest = (balance * monthly_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            principal_payment = (monthly_payment - interest).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            # Final month exact payoff adjustment
            if month == tenure_months or (balance - principal_payment) < Decimal("0.00"):
                principal_payment = balance

            ending_balance = (balance - principal_payment).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            due_date = start_date + timedelta(days=30 * month)

            schedule.append({
                "installment_number": month,
                "due_date": due_date.isoformat(),
                "beginning_balance": balance,
                "monthly_payment": (principal_payment + interest).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
                "principal_payment": principal_payment,
                "interest_payment": interest,
                "ending_balance": ending_balance
            })

            balance = ending_balance
            if balance <= Decimal("0.00"):
                break

        return schedule

    @classmethod
    def classify_cbk_provisioning(cls, days_past_due: int, outstanding_balance: Decimal) -> Dict[str, Any]:
        """
        Central Bank of Kenya (CBK) DCP Regulations 2022 & IFRS 9 Loan Impairment Classification.
        """
        dpd = max(0, days_past_due)
        bal = outstanding_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        if dpd <= 30:
            return {
                "classification": "Normal (Performing)",
                "ifrs9_stage": "Stage 1",
                "provision_rate_percent": Decimal("1.00"),
                "provision_amount": (bal * Decimal("0.01")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
                "risk_tier": "Low"
            }
        elif dpd <= 60:
            return {
                "classification": "Watch (Underperforming)",
                "ifrs9_stage": "Stage 2",
                "provision_rate_percent": Decimal("3.00"),
                "provision_amount": (bal * Decimal("0.03")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
                "risk_tier": "Moderate"
            }
        elif dpd <= 90:
            return {
                "classification": "Substandard (Non-Performing)",
                "ifrs9_stage": "Stage 3",
                "provision_rate_percent": Decimal("20.00"),
                "provision_amount": (bal * Decimal("0.20")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
                "risk_tier": "High"
            }
        elif dpd <= 180:
            return {
                "classification": "Doubtful (Non-Performing)",
                "ifrs9_stage": "Stage 3",
                "provision_rate_percent": Decimal("50.00"),
                "provision_amount": (bal * Decimal("0.50")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
                "risk_tier": "Very High"
            }
        else:
            return {
                "classification": "Loss (Terminal / Write-Off)",
                "ifrs9_stage": "Stage 3",
                "provision_rate_percent": Decimal("100.00"),
                "provision_amount": bal,
                "risk_tier": "Loss"
            }

    @classmethod
    def calculate_par(cls, loans_list: List[Dict[str, Any]], overdue_threshold_days: int = 30) -> Decimal:
        """
        Portfolio at Risk (PAR):
        PAR_N = (Sum of Principal Overdue >= N Days) / (Gross Portfolio Balance) * 100
        """
        if not loans_list:
            return Decimal("0.00")

        total_portfolio = Decimal("0.00")
        overdue_portfolio = Decimal("0.00")

        for loan in loans_list:
            bal = Decimal(str(loan.get("balance", loan.get("principal", "0.00"))))
            dpd = int(loan.get("dpd", 0))
            total_portfolio += bal
            if dpd >= overdue_threshold_days:
                overdue_portfolio += bal

        if total_portfolio == Decimal("0.00"):
            return Decimal("0.00")

        par = (overdue_portfolio / total_portfolio) * Decimal("100")
        return par.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @classmethod
    def calculate_collection_efficiency(cls, actual_recoveries: Decimal, scheduled_due: Decimal) -> Decimal:
        """
        Loan Collection Efficiency:
        CE_t = (Actual Recoveries in Period t) / (Scheduled Due in Period t) * 100
        """
        if scheduled_due <= Decimal("0.00"):
            return Decimal("100.00")
        ce = (actual_recoveries / scheduled_due) * Decimal("100")
        return min(Decimal("100.00"), ce.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
