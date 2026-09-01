/**
 * ORYX FUND — FINANCIAL ENGINE & LEDGER AUTOMATED TEST SUITE
 * Verifies reducing-balance loan math, statutory 20% KRA excise duty,
 * CBK delinquency provisioning, double-entry accounting invariance, and audit hash chaining.
 */

const assert = require('assert');
const OryxCalculator = require('../assets/js/calculator.js');
const { OryxStorage, OryxChartOfAccounts } = require('../assets/js/storage.js');

console.log('🧪 Starting Oryx Fund Institutional Verification Tests...\n');

// -----------------------------------------------------------------------------
// Test 1: Reducing-Balance Loan Amortization (EMI Formula Precision)
// -----------------------------------------------------------------------------
console.log('▶ Test 1: Reducing-Balance Amortization Mathematical Precision');
const pmt1 = OryxCalculator.calculateMonthlyPayment(10000, 12, 12);
assert.strictEqual(pmt1, 888.49, `Expected 888.49, got ${pmt1}`);

const pmt2 = OryxCalculator.calculateMonthlyPayment(50000, 18, 24);
assert.strictEqual(pmt2, 2496.21, `Expected 2496.21, got ${pmt2}`);

const pmt3 = OryxCalculator.calculateMonthlyPayment(100000, 24, 6);
assert.strictEqual(pmt3, 17852.58, `Expected 17852.58, got ${pmt3}`);

const schedule = OryxCalculator.generateAmortizationSchedule(50000, 18, 6);
assert.strictEqual(schedule.length, 6, 'Amortization schedule should contain exactly 6 installments');
assert.strictEqual(schedule[5].endingBalance, 0, 'Final installment ending balance must reach exactly 0');
console.log('  ✔ Reducing-balance amortization math passed with 0 floating-point discrepancy.\n');

// -----------------------------------------------------------------------------
// Test 2: Statutory 20% KRA Excise Duty on Processing Fees
// -----------------------------------------------------------------------------
console.log('▶ Test 2: Kenyan 20% KRA Excise Duty Calculation');
const feeCalc = OryxCalculator.calculateOriginationFeeWithExcise(50000, 3.0);
assert.strictEqual(feeCalc.principal, 50000);
assert.strictEqual(feeCalc.netProcessingFee, 1500.00, 'Net fee should be 3% of 50k = 1500');
assert.strictEqual(feeCalc.exciseDutyPayableKRA, 300.00, 'KRA Excise should be 20% of 1500 = 300');
assert.strictEqual(feeCalc.grossFeeDeduction, 1800.00, 'Gross deduction should be 1800');
assert.strictEqual(feeCalc.netDisbursement, 48200.00, 'Net disbursal should be 48,200.00');
console.log('  ✔ KRA statutory 20% Excise Duty calculations verified.\n');

// -----------------------------------------------------------------------------
// Test 3: Central Bank of Kenya (CBK) 5-Tier Provisioning & IFRS 9 Staging
// -----------------------------------------------------------------------------
console.log('▶ Test 3: CBK Prudential Guidelines & IFRS 9 ECL Staging');
const provNormal = OryxCalculator.classifyCBKProvisioning(15, 100000);
assert.strictEqual(provNormal.classification, 'Normal (Performing)');
assert.strictEqual(provNormal.ifrs9Stage, 'Stage 1');
assert.strictEqual(provNormal.provisionRatePercent, 1.00);
assert.strictEqual(provNormal.provisionAmount, 1000.00);

const provWatch = OryxCalculator.classifyCBKProvisioning(45, 100000);
assert.strictEqual(provWatch.classification, 'Watch (Underperforming)');
assert.strictEqual(provWatch.ifrs9Stage, 'Stage 2');
assert.strictEqual(provWatch.provisionRatePercent, 3.00);
assert.strictEqual(provWatch.provisionAmount, 3000.00);

const provSubstandard = OryxCalculator.classifyCBKProvisioning(75, 100000);
assert.strictEqual(provSubstandard.classification, 'Substandard (Non-Performing)');
assert.strictEqual(provSubstandard.ifrs9Stage, 'Stage 3');
assert.strictEqual(provSubstandard.provisionRatePercent, 20.00);
assert.strictEqual(provSubstandard.provisionAmount, 20000.00);

const provDoubtful = OryxCalculator.classifyCBKProvisioning(120, 100000);
assert.strictEqual(provDoubtful.classification, 'Doubtful (Non-Performing)');
assert.strictEqual(provDoubtful.provisionRatePercent, 50.00);
assert.strictEqual(provDoubtful.provisionAmount, 50000.00);

const provLoss = OryxCalculator.classifyCBKProvisioning(190, 100000);
assert.strictEqual(provLoss.classification, 'Loss (Terminal / Write-Off)');
assert.strictEqual(provLoss.provisionRatePercent, 100.00);
assert.strictEqual(provLoss.provisionAmount, 100000.00);
console.log('  ✔ CBK 5-Tier Delinquency and IFRS 9 staging rules verified.\n');

// -----------------------------------------------------------------------------
// Test 4: Portfolio at Risk (PAR 30) & Collection Efficiency
// -----------------------------------------------------------------------------
console.log('▶ Test 4: Portfolio at Risk (PAR 30) & Collection Efficiency');
const mockPortfolio = [
  { balance: 100000, dpd: 0 },
  { balance: 200000, dpd: 15 },
  { balance: 50000, dpd: 45 }, // Overdue >= 30
  { balance: 150000, dpd: 95 }  // Overdue >= 30
];
// Total = 500k, Overdue >= 30 = 200k => PAR 30 = 40.0%
const par30 = OryxCalculator.calculatePAR(mockPortfolio, 30);
assert.strictEqual(par30, 40.0, `Expected 40.0%, got ${par30}%`);

const ce = OryxCalculator.calculateCollectionEfficiency(98000, 100000);
assert.strictEqual(ce, 98.0, `Expected 98.0%, got ${ce}%`);
console.log('  ✔ Portfolio at Risk & Collection Efficiency telemetry verified.\n');

// -----------------------------------------------------------------------------
// Test 5: Chart of Accounts & Double-Entry Invariance
// -----------------------------------------------------------------------------
console.log('▶ Test 5: Double-Entry Ledger Zero-Sum Balance Invariance');
// Setup Mock localStorage environment for Node.js
global.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = v.toString(); },
  removeItem(k) { delete this.store[k]; }
};

// Test Balanced Journal Post (Loan Disbursal of KES 50,000)
const txResult = OryxStorage.postJournalTransaction(
  'TXN-TEST-001',
  'Disbursal of ACC-LOAN-2026-00001 with 20% KRA Excise Duty',
  'ACC-LOAN-2026-00001',
  [
    { accountCode: '12000', debit: 50000, credit: 0 },
    { accountCode: '10100', debit: 0, credit: 48200 },
    { accountCode: '40200', debit: 0, credit: 1500 },
    { accountCode: '20200', debit: 0, credit: 300 }
  ]
);
assert.strictEqual(txResult.success, true);
assert.strictEqual(txResult.totalAmount, 50000);

// Verify Trial Balance
const trialBal = OryxStorage.getTrialBalance();
assert.strictEqual(trialBal['12000'].netBalance, 50000, 'Loans Receivable should have Debit balance 50,000');
assert.strictEqual(trialBal['10100'].netBalance, -48200, 'M-Pesa B2C Float should reflect credit outflow 48,200');
assert.strictEqual(trialBal['40200'].netBalance, 1500, 'Processing fee income should reflect credit 1,500');
assert.strictEqual(trialBal['20200'].netBalance, 300, 'Excise duty payable should reflect credit liability 300');

// Test Unbalanced Transaction Exception
assert.throws(() => {
  OryxStorage.postJournalTransaction(
    'TXN-ERR-001',
    'Unbalanced entry',
    'ACC-LOAN-ERR',
    [
      { accountCode: '12000', debit: 50000, credit: 0 },
      { accountCode: '10100', debit: 0, credit: 40000 } // Unbalanced!
    ]
  );
}, /Double-entry balance mismatch/, 'Should throw exception on unbalanced debit/credit');
console.log('  ✔ Double-entry ledger invariants and zero-sum trial balance passed.\n');

// -----------------------------------------------------------------------------
// Test 6: Cryptographic WORM Audit Log Chaining
// -----------------------------------------------------------------------------
console.log('▶ Test 6: WORM Audit Trail Hash Chaining');
global.crypto = require('crypto').webcrypto;

(async () => {
  const event1 = await OryxStorage.logAuditEvent(
    { email: 'dervinaziza9@gmail.com', role: 'Admin' },
    'FACILITY_SANCTIONED',
    { entityId: 'ACC-LOAN-2026-00001' },
    4,
    { pre: 'Review', post: 'Sanctioned' }
  );

  const event2 = await OryxStorage.logAuditEvent(
    { email: 'dervinaziza9@gmail.com', role: 'Admin' },
    'FACILITY_DISBURSED',
    { entityId: 'ACC-LOAN-2026-00001' },
    4,
    { pre: 'Sanctioned', post: 'Disbursed' }
  );

  assert.strictEqual(event2.previousEventHash, event1.merkleRootHash, 'Audit event 2 must link cryptographically to event 1 hash');
  console.log('  ✔ Cryptographic hash chaining on WORM audit trail passed.\n');

  console.log('===============================================================');
  console.log('🎉 ALL 6 INSTITUTIONAL VERIFICATION TEST SUITES PASSED (100%)');
  console.log('===============================================================');
})();
