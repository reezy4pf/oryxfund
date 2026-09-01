/**
 * ORYX FUND — FINANCIAL CALCULATION & RISK ENGINE (assets/js/calculator.js)
 * Implements standard reducing-balance loan amortization, statutory KRA 20% excise duty,
 * CBK Prudential Guidelines / IFRS 9 loan impairment provisioning, and portfolio risk telemetry.
 */

const OryxCalculator = {
  // Statutory Kenyan KRA Excise Duty on Processing/Origination Fees
  STATUTORY_EXCISE_DUTY_RATE: 0.20,

  /**
   * Calculate monthly loan repayment using standard reducing-balance amortization (EMI):
   * EMI = [P x r x (1+r)^n] / [(1+r)^n - 1]
   */
  calculateMonthlyPayment(principal, annualRatePercent, tenureMonths) {
    const p = parseFloat(principal) || 0;
    const n = parseInt(tenureMonths, 10) || 1;
    const r = (parseFloat(annualRatePercent) || 14) / 100 / 12;

    if (r === 0 || p === 0) return Math.round((p / n) * 100) / 100;
    const factor = Math.pow(1 + r, n);
    const emi = (p * r * factor) / (factor - 1);
    return Math.round(emi * 100) / 100;
  },

  calculateTotalRepayment(principal, annualRatePercent, tenureMonths) {
    const monthly = this.calculateMonthlyPayment(principal, annualRatePercent, tenureMonths);
    return Math.round(monthly * tenureMonths * 100) / 100;
  },

  calculateTotalInterest(principal, annualRatePercent, tenureMonths) {
    const total = this.calculateTotalRepayment(principal, annualRatePercent, tenureMonths);
    return Math.round((total - principal) * 100) / 100;
  },

  /**
   * Generates a complete periodic reducing-balance amortization schedule.
   */
  generateAmortizationSchedule(principal, annualRatePercent, tenureMonths, startDate = new Date()) {
    const schedule = [];
    let balance = parseFloat(principal) || 0;
    const monthlyPayment = this.calculateMonthlyPayment(principal, annualRatePercent, tenureMonths);
    const monthlyRate = (parseFloat(annualRatePercent) || 14) / 100 / 12;

    for (let month = 1; month <= tenureMonths; month++) {
      const interest = Math.round(balance * monthlyRate * 100) / 100;
      let principalPayment = Math.round((monthlyPayment - interest) * 100) / 100;
      
      // Final month adjustment for exact balance payoff
      if (month === tenureMonths || balance - principalPayment < 0) {
        principalPayment = balance;
      }
      const endingBalance = Math.max(0, Math.round((balance - principalPayment) * 100) / 100);

      const dueDate = new Date(startDate);
      dueDate.setMonth(dueDate.getMonth() + month);

      schedule.push({
        installmentNumber: month,
        dueDate: dueDate.toISOString().split('T')[0],
        beginningBalance: balance,
        monthlyPayment: Math.round((principalPayment + interest) * 100) / 100,
        principalPayment: principalPayment,
        interestPayment: interest,
        endingBalance: endingBalance
      });

      balance = endingBalance;
      if (balance <= 0) break;
    }

    return schedule;
  },

  /**
   * Calculate statutory Kenyan KRA 20% Excise Duty on processing and facility appraisal fees.
   * Net Processing Fee = Principal * Fee Rate
   * Excise Duty (KRA) = Net Fee * 20%
   * Gross Fee Deduction = Net Fee + Excise Duty
   * Net Disbursal Amount = Principal - Gross Fee Deduction
   */
  calculateOriginationFeeWithExcise(principal, feeRatePercent = 2.0) {
    const p = parseFloat(principal) || 0;
    const netFee = Math.round(p * (feeRatePercent / 100) * 100) / 100;
    const exciseDuty = Math.round(netFee * this.STATUTORY_EXCISE_DUTY_RATE * 100) / 100;
    const grossFee = Math.round((netFee + exciseDuty) * 100) / 100;
    const netDisbursement = Math.max(0, Math.round((p - grossFee) * 100) / 100);

    return {
      principal: p,
      feeRatePercent: feeRatePercent,
      netProcessingFee: netFee,
      exciseDutyPayableKRA: exciseDuty,
      grossFeeDeduction: grossFee,
      netDisbursement: netDisbursement
    };
  },

  /**
   * Central Bank of Kenya (CBK) Prudential Guidelines & IFRS 9 Loan Loss Classification:
   * Categorizes loan facilities into aging delinquency buckets and calculates minimum regulatory provisions.
   */
  classifyCBKProvisioning(daysPastDue, outstandingBalance) {
    const dpd = parseInt(daysPastDue, 10) || 0;
    const balance = parseFloat(outstandingBalance) || 0;

    if (dpd <= 30) {
      return {
        classification: 'Normal (Performing)',
        ifrs9Stage: 'Stage 1',
        provisionRatePercent: 1.00,
        provisionAmount: Math.round(balance * 0.01 * 100) / 100,
        riskTier: 'Low',
        color: '#00D26A'
      };
    } else if (dpd <= 60) {
      return {
        classification: 'Watch (Underperforming)',
        ifrs9Stage: 'Stage 2',
        provisionRatePercent: 3.00,
        provisionAmount: Math.round(balance * 0.03 * 100) / 100,
        riskTier: 'Moderate',
        color: '#FBBF24'
      };
    } else if (dpd <= 90) {
      return {
        classification: 'Substandard (Non-Performing)',
        ifrs9Stage: 'Stage 3',
        provisionRatePercent: 20.00,
        provisionAmount: Math.round(balance * 0.20 * 100) / 100,
        riskTier: 'High',
        color: '#F97316'
      };
    } else if (dpd <= 180) {
      return {
        classification: 'Doubtful (Non-Performing)',
        ifrs9Stage: 'Stage 3',
        provisionRatePercent: 50.00,
        provisionAmount: Math.round(balance * 0.50 * 100) / 100,
        riskTier: 'Very High',
        color: '#EF4444'
      };
    } else {
      return {
        classification: 'Loss (Terminal / Write-Off)',
        ifrs9Stage: 'Stage 3',
        provisionRatePercent: 100.00,
        provisionAmount: balance,
        riskTier: 'Loss',
        color: '#7F1D1D'
      };
    }
  },

  /**
   * Portfolio at Risk (PAR) Telemetry:
   * PAR_N = (Sum of Principal of Loans Overdue >= N Days) / (Gross Portfolio Balance) * 100
   */
  calculatePAR(loansArray, overdueThresholdDays = 30) {
    if (!Array.isArray(loansArray) || loansArray.length === 0) return 0;

    let totalPortfolio = 0;
    let parOverdueBalance = 0;

    loansArray.forEach(loan => {
      const balance = parseFloat(loan.balance || loan.principal || 0);
      const dpd = parseInt(loan.dpd || 0, 10);
      totalPortfolio += balance;
      if (dpd >= overdueThresholdDays) {
        parOverdueBalance += balance;
      }
    });

    if (totalPortfolio === 0) return 0;
    return Math.round((parOverdueBalance / totalPortfolio) * 10000) / 100;
  },

  /**
   * Loan Collection Efficiency Rate:
   * CE_t = (Actual Cash Recoveries in Period t) / (Contractually Scheduled Due in Period t) * 100
   */
  calculateCollectionEfficiency(actualRecoveries, scheduledPaymentsDue) {
    const actual = parseFloat(actualRecoveries) || 0;
    const scheduled = parseFloat(scheduledPaymentsDue) || 0;
    if (scheduled <= 0) return 100.0;
    return Math.min(100, Math.round((actual / scheduled) * 10000) / 100);
  },

  /**
   * Calculate Debt-to-Income (DTI) Ratio:
   * DTI = ((Existing Monthly Debt + New Monthly EMI) / Gross or Net Monthly Income) * 100
   */
  calculateDTI(monthlyIncome, existingMonthlyDebt, newMonthlyRepayment) {
    const income = parseFloat(monthlyIncome) || 0;
    const debt = (parseFloat(existingMonthlyDebt) || 0) + (parseFloat(newMonthlyRepayment) || 0);

    if (income <= 0) return 0;
    const dti = (debt / income) * 100;
    return Math.min(100, Math.max(0, Math.round(dti * 10) / 10));
  },

  getDTIScoreBand(dtiPercent) {
    if (dtiPercent <= 35) return { label: 'Optimal (Tier 1)', color: '#00D26A', risk: 'Low' };
    if (dtiPercent <= 45) return { label: 'Acceptable (Tier 2)', color: '#34D399', risk: 'Moderate' };
    if (dtiPercent <= 50) return { label: 'Conditional (Tier 3)', color: '#FBBF24', risk: 'Elevated' };
    return { label: 'Restricted (High Risk)', color: '#EF4444', risk: 'High' };
  }
};

// Node.js module export support for automated unit test harnesses
if (typeof module !== 'undefined' && module.exports) {
  module.exports = OryxCalculator;
}
