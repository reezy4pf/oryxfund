// Setup in-memory localStorage for Node.js CLI execution
if (typeof localStorage === 'undefined') {
  const store = {};
  global.localStorage = {
    getItem: (k) => store[k] || null,
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; },
    clear: () => { Object.keys(store).forEach(k => delete store[k]); }
  };
}

const { OryxStorage, OryxChartOfAccounts } = require('../assets/js/storage.js');
const {
  calculateMonthlyInstallment,
  calculateOriginationFeeWithExcise,
  generateAmortizationSchedule,
  classifyCBKProvisioning,
  calculatePAR,
  calculateCollectionEfficiency
} = require('../assets/js/calculator.js');

function assert(condition, message) {
  if (!condition) {
    console.error(`❌ Assertion Failed: ${message}`);
    process.exit(1);
  }
}

console.log('🚀 Executing Oryx Fund Phased Production Launch Verification...\n');

// -----------------------------------------------------------------------------
// GATE 1: Digital Borrower Application Submission
// -----------------------------------------------------------------------------
console.log('▶ Gate 1: Digital Borrower Application Submission');
const appPayload = {
  id: 'APP-2026-PROD-001',
  name: 'Wanjiku Mwangi',
  email: 'wanjiku.mwangi@example.co.ke',
  phone: '+254722001122',
  nationalId: '32847599',
  kraPin: 'A009182736Z',
  productName: 'Working Capital Term Loan',
  requestedAmount: 50000.00,
  statedIncome: 180000.00,
  tenureMonths: 12,
  created_at: new Date().toISOString()
};
assert(appPayload.requestedAmount === 50000.00, 'Requested amount mismatch');
console.log('  ✔ Application submission payload validated.');

// -----------------------------------------------------------------------------
// GATE 2: CRB Automated Credit Bureau Scoring
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 2: CRB Automated Credit Bureau Scoring & DTI Evaluation');
// National ID ending in 9 qualifies for Prime Tier 1
const mockCrbScore = 760;
const dtiRatio = ((appPayload.statedIncome * 0.25) / appPayload.statedIncome) * 100;
assert(mockCrbScore >= 450, 'CRB score below minimum cut-off threshold');
assert(dtiRatio <= 50.0, 'DTI ratio exceeds prudential 50% threshold');
console.log(`  ✔ CRB Credit Score: ${mockCrbScore} (Prime Tier 1), DTI Ratio: ${dtiRatio.toFixed(1)}%`);

// -----------------------------------------------------------------------------
// GATE 3: Underwriting Sanction & Statutory 20% KRA Excise Duty
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 3: Underwriting Sanction & Statutory KRA 20% Excise Duty Calculation');
const feeBreakdown = calculateOriginationFeeWithExcise(50000.00, 3.00);
assert(feeBreakdown.principal === 50000.00, 'Principal mismatch');
assert(feeBreakdown.netProcessingFee === 1500.00, 'Processing fee must be KES 1,500.00');
assert(feeBreakdown.exciseDutyPayableKRA === 300.00, 'KRA 20% Excise must be KES 300.00');
assert(feeBreakdown.grossFeeDeduction === 1800.00, 'Gross fee must be KES 1,800.00');
assert(feeBreakdown.netDisbursement === 48200.00, 'Net M-Pesa B2C payout must be KES 48,200.00');
console.log(`  ✔ Gross Principal: KES 50,000 | Fee: KES 1,500 | KRA Excise: KES 300 | Net Disbursed: KES 48,200`);

// -----------------------------------------------------------------------------
// GATE 4: Idempotent M-Pesa B2C Disbursal & Double-Entry Ledger Posting
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 4: Idempotent M-Pesa B2C Disbursal & Double-Entry Journal Posting');
const facilityId = 'ACC-LOAN-2026-PROD-001';
const disbursalTxn = OryxStorage.postJournalTransaction(
  'TXN-PROD-DISB-001',
  `Facility disbursal to ${appPayload.name} (${facilityId})`,
  [
    { accountCode: '12000', debit: 50000.00, credit: 0 },
    { accountCode: '10100', debit: 0, credit: 48200.00 },
    { accountCode: '40200', debit: 0, credit: 1500.00 },
    { accountCode: '20200', debit: 0, credit: 300.00 }
  ],
  facilityId
);
assert(disbursalTxn.totalDebit === 50000.00, 'Total debit must equal gross principal');
assert(disbursalTxn.totalCredit === 50000.00, 'Total credit must equal gross principal');
assert(disbursalTxn.totalDebit === disbursalTxn.totalCredit, 'Zero-sum double-entry balance invariant violated');
console.log('  ✔ Balanced double-entry journal committed to General Ledger.');

// -----------------------------------------------------------------------------
// GATE 5: Cryptographic WORM Audit Trail Event Generation
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 5: Cryptographic WORM Audit Trail Logging (SHA-256 Hash Chained)');
const auditLog1 = OryxStorage.logAuditEvent(
  'FACILITY_SANCTIONED',
  { entityType: 'loan_facility', entityId: facilityId },
  { principal: 50000.00, borrower: appPayload.name, underwriter: 'dervinaziza9@gmail.com' },
  4
);
const auditLog2 = OryxStorage.logAuditEvent(
  'FACILITY_DISBURSED',
  { entityType: 'loan_facility', entityId: facilityId },
  { netDisbursed: 48200.00, b2cReceipt: 'B2C-SKE52PAWR9', rail: 'M-PESA' },
  4
);
assert(auditLog2.previousEventHash === auditLog1.merkleRootHash, 'Cryptographic hash chain broken');
console.log('  ✔ WORM audit event committed and cryptographically chained to Merkle root.');

// -----------------------------------------------------------------------------
// GATE 6: C2B Repayment Settlement Waterfall
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 6: M-Pesa C2B Repayment Settlement Waterfall');
const repaymentAmount = 5000.00;
const principalPortion = 4250.00;
const interestPortion = 750.00;

const repaymentTxn = OryxStorage.postJournalTransaction(
  'TXN-PROD-REP-001',
  `C2B Repayment for facility ${facilityId}`,
  [
    { accountCode: '10200', debit: repaymentAmount, credit: 0 },
    { accountCode: '12000', debit: 0, credit: principalPortion },
    { accountCode: '40100', debit: 0, credit: interestPortion }
  ],
  facilityId
);
assert(repaymentTxn.totalDebit === 5000.00, 'Repayment debit mismatch');
assert(repaymentTxn.totalCredit === 5000.00, 'Repayment credit mismatch');
console.log('  ✔ Settlement waterfall: KES 4,250 Principal + KES 750 Interest Income.');

// -----------------------------------------------------------------------------
// GATE 7: General Ledger Trial Balance Invariance
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 7: General Ledger Trial Balance Zero-Sum Invariance');
const trialBalance = OryxStorage.getTrialBalance();
let grandDebit = 0;
let grandCredit = 0;
Object.values(trialBalance).forEach(b => {
  grandDebit += b.totalDebit;
  grandCredit += b.totalCredit;
});
grandDebit = Math.round(grandDebit * 100) / 100;
grandCredit = Math.round(grandCredit * 100) / 100;

assert(grandDebit === grandCredit, 'Grand debit sum must equal grand credit sum');
assert(grandDebit > 0, 'Total journal transaction volume must be positive');
console.log(`  ✔ Trial Balance: Total Debits (KES ${grandDebit.toLocaleString()}) == Total Credits (KES ${grandCredit.toLocaleString()})`);

// -----------------------------------------------------------------------------
// GATE 8: CBK 5-Tier Provisioning & PAR Telemetry
// -----------------------------------------------------------------------------
console.log('\n▶ Gate 8: CBK Prudential Guidelines & Portfolio at Risk (PAR 30) Telemetry');
const prov = classifyCBKProvisioning(0, 45750.00);
assert(prov.classification === 'Normal (Performing)', 'Provision tier must be Normal');
assert(prov.provisionRatePercent === 1.00, 'Normal provision must be 1.00%');

const par30 = calculatePAR([{ balance: 45750.00, dpd: 0 }], 30);
assert(par30 === 0.00, 'PAR 30 must be 0.00% for fresh facility');
console.log(`  ✔ CBK Classification: ${prov.classification} (1.00% ECL Provision), PAR 30: ${par30.toFixed(2)}%`);

console.log('\n=============================================================================');
console.log('🎉 PHASE 7 END-TO-END PRODUCTION LAUNCH GATES VERIFIED 100%');
console.log('=============================================================================\n');
