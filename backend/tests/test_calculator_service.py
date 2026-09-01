"""
ORYX FUND — FINANCIAL CALCULATOR UNIT TESTS (backend/tests/test_calculator_service.py)
Validates high-precision Decimal loan amortization, statutory KRA 20% excise duty,
CBK 5-tier provisioning, PAR 30, and collection efficiency.
"""

from decimal import Decimal
import pytest
from backend.app.services.calculator_service import CalculatorService

def test_reducing_balance_amortization_precision():
    # 10k KES at 12% for 12 months -> exactly 888.49
    pmt1 = CalculatorService.calculate_monthly_installment(Decimal("10000.00"), Decimal("12.00"), 12)
    assert pmt1 == Decimal("888.49")

    # 50k KES at 18% for 24 months -> exactly 2496.21
    pmt2 = CalculatorService.calculate_monthly_installment(Decimal("50000.00"), Decimal("18.00"), 24)
    assert pmt2 == Decimal("2496.21")

    # 100k KES at 24% for 6 months -> exactly 17852.58
    pmt3 = CalculatorService.calculate_monthly_installment(Decimal("100000.00"), Decimal("24.00"), 6)
    assert pmt3 == Decimal("17852.58")

def test_amortization_schedule_full_payoff():
    schedule = CalculatorService.generate_amortization_schedule(Decimal("50000.00"), Decimal("18.00"), 6)
    assert len(schedule) == 6
    assert schedule[0]["installment_number"] == 1
    assert schedule[-1]["installment_number"] == 6
    assert schedule[-1]["ending_balance"] == Decimal("0.00")

def test_statutory_kra_excise_duty_calculation():
    # Facility of 50,000 KES with 3% origination fee
    fee_calc = CalculatorService.calculate_origination_fee_with_excise(Decimal("50000.00"), Decimal("3.00"))
    assert fee_calc["principal"] == Decimal("50000.00")
    assert fee_calc["net_processing_fee"] == Decimal("1500.00")
    assert fee_calc["excise_duty_payable_kra"] == Decimal("300.00")
    assert fee_calc["gross_fee_deduction"] == Decimal("1800.00")
    assert fee_calc["net_disbursement"] == Decimal("48200.00")

def test_cbk_prudential_provisioning_tiers():
    # Normal (0-30 DPD) -> 1.00%
    prov_normal = CalculatorService.classify_cbk_provisioning(15, Decimal("100000.00"))
    assert prov_normal["classification"] == "Normal (Performing)"
    assert prov_normal["provision_rate_percent"] == Decimal("1.00")
    assert prov_normal["provision_amount"] == Decimal("1000.00")

    # Watch (31-60 DPD) -> 3.00%
    prov_watch = CalculatorService.classify_cbk_provisioning(45, Decimal("100000.00"))
    assert prov_watch["classification"] == "Watch (Underperforming)"
    assert prov_watch["provision_rate_percent"] == Decimal("3.00")
    assert prov_watch["provision_amount"] == Decimal("3000.00")

    # Substandard (61-90 DPD) -> 20.00%
    prov_sub = CalculatorService.classify_cbk_provisioning(75, Decimal("100000.00"))
    assert prov_sub["classification"] == "Substandard (Non-Performing)"
    assert prov_sub["provision_rate_percent"] == Decimal("20.00")
    assert prov_sub["provision_amount"] == Decimal("20000.00")

    # Doubtful (91-180 DPD) -> 50.00%
    prov_doubt = CalculatorService.classify_cbk_provisioning(120, Decimal("100000.00"))
    assert prov_doubt["classification"] == "Doubtful (Non-Performing)"
    assert prov_doubt["provision_rate_percent"] == Decimal("50.00")
    assert prov_doubt["provision_amount"] == Decimal("50000.00")

    # Loss (180+ DPD) -> 100.00%
    prov_loss = CalculatorService.classify_cbk_provisioning(200, Decimal("100000.00"))
    assert prov_loss["classification"] == "Loss (Terminal / Write-Off)"
    assert prov_loss["provision_rate_percent"] == Decimal("100.00")
    assert prov_loss["provision_amount"] == Decimal("100000.00")

def test_portfolio_at_risk_and_collection_efficiency():
    mock_loans = [
        {"balance": "100000.00", "dpd": 0},
        {"balance": "200000.00", "dpd": 10},
        {"balance": "50000.00", "dpd": 35},  # Overdue >= 30
        {"balance": "150000.00", "dpd": 90}  # Overdue >= 30
    ]
    # Total = 500k, Overdue = 200k => PAR 30 = 40.00%
    par30 = CalculatorService.calculate_par(mock_loans, 30)
    assert par30 == Decimal("40.00")

    ce = CalculatorService.calculate_collection_efficiency(Decimal("98000.00"), Decimal("100000.00"))
    assert ce == Decimal("98.00")
