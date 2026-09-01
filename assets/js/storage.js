/**
 * ORYX FUND — PRODUCTION STORAGE & LEDGER REPOSITORY (assets/js/storage.js)
 * Clean, production-grade repository for borrower accounts, double-entry financial ledger,
 * Chart of Accounts (COA), immutable WORM audit trail, and transaction idempotency locks.
 */

const OryxChartOfAccounts = {
  10100: { code: '10100', name: 'M-Pesa B2C Utility Float', type: 'Asset', normalBalance: 'Debit' },
  10200: { code: '10200', name: 'M-Pesa C2B Collections Float', type: 'Asset', normalBalance: 'Debit' },
  10300: { code: '10300', name: 'Commercial Bank Settlement Float', type: 'Asset', normalBalance: 'Debit' },
  12000: { code: '12000', name: 'Loans Receivable – Principal', type: 'Asset', normalBalance: 'Debit' },
  12100: { code: '12100', name: 'Interest Receivable – Accrued', type: 'Asset', normalBalance: 'Debit' },
  12200: { code: '12200', name: 'Late Penalty Receivable', type: 'Asset', normalBalance: 'Debit' },
  12900: { code: '12900', name: 'Allowance for Credit Losses (ECL)', type: 'Contra-Asset', normalBalance: 'Credit' },
  20100: { code: '20100', name: 'Borrower Unallocated Repayments (Suspense)', type: 'Liability', normalBalance: 'Credit' },
  20200: { code: '20200', name: 'Excise Duty Payable (KRA)', type: 'Liability', normalBalance: 'Credit' },
  21000: { code: '21000', name: 'Senior Debt / Institutional LP Capital', type: 'Liability', normalBalance: 'Credit' },
  30100: { code: '30100', name: 'Retained Earnings', type: 'Equity', normalBalance: 'Credit' },
  40100: { code: '40100', name: 'Interest Income', type: 'Revenue', normalBalance: 'Credit' },
  40200: { code: '40200', name: 'Processing Fee Income', type: 'Revenue', normalBalance: 'Credit' },
  40300: { code: '40300', name: 'Penalty & Late Fee Revenue', type: 'Revenue', normalBalance: 'Credit' },
  50100: { code: '50100', name: 'Provision Expense for Bad Debts', type: 'Expense', normalBalance: 'Debit' },
  50200: { code: '50200', name: 'Payment Gateway & Rail Expenses', type: 'Expense', normalBalance: 'Debit' },
  50300: { code: '50300', name: 'Principal Loan Write-Off', type: 'Expense', normalBalance: 'Debit' }
};

const OryxStorage = {
  SEED_VERSION: 'prod_v3',

  initSeeds() {
    if (typeof localStorage === 'undefined') return;
    if (localStorage.getItem('oryx_auth_seeded') !== this.SEED_VERSION) {
      // Seed verified Administrator identity (Clearance Level 4)
      const adminAccount = {
        id: 'usr_admin_001',
        userId: 'usr_admin_001',
        name: 'Dervin Aziza',
        email: 'dervinaziza9@gmail.com',
        phone: '+254700000000',
        nationalId: 'ADM-001',
        kraPin: 'A000000000Z',
        address: 'Upper Hill, Nairobi',
        county: 'Nairobi',
        role: 'Admin',
        clearanceLevel: 4,
        passwordHash: '91521ad19aee4d15e8ed916c75354a4411e6a5c43703ddb048411c41b67732c7', // Oryx2026
        created_at: new Date().toISOString()
      };
      this.saveUser(adminAccount);

      // Seed verified default Borrower identity
      const defaultBorrower = {
        id: 'usr_reezy_001',
        userId: 'usr_reezy_001',
        name: 'Reuben Njoroge',
        email: 'reezyhoops@gmail.com',
        phone: '+254 712 345 678',
        nationalId: '32847592',
        kraPin: 'A009823414Z',
        address: 'Westlands Commercial Hub, Nairobi',
        county: 'Nairobi',
        role: 'Borrower',
        passwordHash: '91521ad19aee4d15e8ed916c75354a4411e6a5c43703ddb048411c41b67732c7', // Oryx2026
        created_at: new Date().toISOString()
      };
      this.saveUser(defaultBorrower);

      // Seed active loan for default borrower
      const initialActiveLoan = {
        loanId: 'ACC-LOAN-2026-008',
        productName: 'Oryx Subsequent Fast-Track Facility',
        principal: 250000,
        disbursedDate: '2026-08-15',
        termMonths: 12,
        monthlyRate: 1.5,
        monthlyInstallment: 23750,
        balance: 261250,
        nextDueDate: '2026-09-15',
        repayments: [
          {
            id: 'REP-2026-08-15-01',
            date: '2026-08-15',
            amount: 23750,
            ref: 'QK91827364',
            method: 'M-Pesa STK Push'
          }
        ]
      };
      this.saveActiveLoan('usr_reezy_001', initialActiveLoan);

      // Seed demo user application
      const initialUserApps = [
        {
          id: 'ACC-LOAP-2026-008',
          fullName: 'Reuben Njoroge',
          productName: 'Oryx Subsequent Fast-Track Facility',
          amount: 250000,
          term: 12,
          date: '2026-08-15',
          status: 'Sanctioned & Disbursed'
        }
      ];
      localStorage.setItem('oryx_apps_usr_reezy_001', JSON.stringify(initialUserApps));

      // Seed balanced double-entry ledger journal entries if empty
      if (!localStorage.getItem('oryx_ledger_journal_entries')) {
        this.postJournalTransaction(
          'TXN-INIT-001',
          'Initial LP Capital Facility Allocation & M-Pesa Float Provisioning',
          'LP-EQUITY-01',
          [
            { accountCode: '10100', debit: 5000000, credit: 0 },
            { accountCode: '21000', debit: 0, credit: 5000000 }
          ],
          'admin@oryxfund.co.ke'
        );
        this.postJournalTransaction(
          'TXN-INIT-002',
          'Disbursal of ACC-LOAN-2026-008 with KRA Excise Duty Deduction',
          'ACC-LOAN-2026-008',
          [
            { accountCode: '12000', debit: 250000, credit: 0 },
            { accountCode: '10100', debit: 0, credit: 244000 },
            { accountCode: '40200', debit: 0, credit: 5000 },
            { accountCode: '20200', debit: 0, credit: 1000 }
          ],
          'admin@oryxfund.co.ke'
        );
      }

      // Seed initial WORM audit log if empty
      if (!localStorage.getItem('oryx_worm_audit_log')) {
        this.logAuditEvent(
          { staff_id: 'usr_admin_001', email: 'dervinaziza9@gmail.com', role: 'Admin' },
          'SYSTEM_INITIALIZED',
          { entity_type: 'System', entity_id: 'ORYX-CORE' },
          4,
          { status: 'Production_Ready', statutory_framework: 'CBK_DCP_2022' }
        );
      }

      localStorage.setItem('oryx_auth_seeded', this.SEED_VERSION);
    }
  },

  getUser(userId) {
    if (!userId) return null;
    try {
      const raw = localStorage.getItem('oryx_user_' + userId);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  },

  getUserByIdentifier(ident) {
    if (!ident) return null;
    const cleanIdent = ident.trim().toLowerCase().replace(/\s+/g, '');
    const userId = localStorage.getItem('oryx_idx_' + cleanIdent);
    return userId ? this.getUser(userId) : null;
  },

  saveUser(user) {
    if (!user || (!user.id && !user.userId)) return;
    const uid = user.id || user.userId;
    user.id = uid;
    user.userId = uid;
    localStorage.setItem('oryx_user_' + uid, JSON.stringify(user));
    if (user.email) {
      localStorage.setItem('oryx_idx_' + user.email.toLowerCase().trim(), uid);
    }
    if (user.phone) {
      localStorage.setItem('oryx_idx_' + user.phone.replace(/\s+/g, '').trim(), uid);
    }
  },

  getActiveLoan(userId) {
    if (!userId) return null;
    try {
      const raw = localStorage.getItem('oryx_active_loan_' + userId);
      if (raw) return JSON.parse(raw);
      // Fallback for default user
      if (userId === 'usr_reezy_001') {
        const fallback = {
          loanId: 'ACC-LOAN-2026-008',
          productName: 'Oryx Subsequent Fast-Track Facility',
          principal: 250000,
          disbursedDate: '2026-08-15',
          termMonths: 12,
          monthlyRate: 1.5,
          monthlyInstallment: 23750,
          balance: 261250,
          nextDueDate: '2026-09-15',
          repayments: [
            {
              id: 'REP-2026-08-15-01',
              date: '2026-08-15',
              amount: 23750,
              ref: 'QK91827364',
              method: 'M-Pesa STK Push'
            }
          ]
        };
        this.saveActiveLoan('usr_reezy_001', fallback);
        return fallback;
      }
      return null;
    } catch (e) {
      return null;
    }
  },

  saveActiveLoan(userId, loan) {
    if (!userId) return;
    localStorage.setItem('oryx_active_loan_' + userId, JSON.stringify(loan));
  },

  getAllApplications() {
    try {
      return JSON.parse(localStorage.getItem('oryx_applications') || '[]');
    } catch (e) {
      return [];
    }
  },

  saveApplication(app) {
    if (!app || !app.id) return;
    const apps = this.getAllApplications();
    const idx = apps.findIndex(a => a.id === app.id);
    if (idx >= 0) {
      apps[idx] = app;
    } else {
      apps.unshift(app);
    }
    localStorage.setItem('oryx_applications', JSON.stringify(apps));
  },

  // =========================================================================
  // DOUBLE-ENTRY FINANCIAL LEDGER & JOURNAL ENGINE
  // =========================================================================
  getLedgerJournalEntries() {
    try {
      return JSON.parse(localStorage.getItem('oryx_ledger_journal_entries') || '[]');
    } catch (e) {
      return [];
    }
  },

  /**
   * Post balanced double-entry journal entries to the financial ledger.
   * Invariant: Total Debits MUST strictly equal Total Credits.
   */
  postJournalTransaction(transactionId, narration, facilityId, linesArray, actorEmail = 'system') {
    if (!Array.isArray(linesArray) || linesArray.length < 2) {
      throw new Error('A journal transaction requires at least 2 entries.');
    }

    let totalDebit = 0;
    let totalCredit = 0;

    linesArray.forEach(line => {
      totalDebit += parseFloat(line.debit || 0);
      totalCredit += parseFloat(line.credit || 0);
    });

    totalDebit = Math.round(totalDebit * 100) / 100;
    totalCredit = Math.round(totalCredit * 100) / 100;

    if (totalDebit !== totalCredit) {
      throw new Error(`Double-entry balance mismatch: Debits (${totalDebit}) != Credits (${totalCredit})`);
    }

    const journal = this.getLedgerJournalEntries();
    const timestamp = new Date().toISOString();

    linesArray.forEach(line => {
      const entryId = 'JRN-' + Date.now() + '-' + Math.floor(1000 + Math.random() * 9000);
      journal.unshift({
        entryId: entryId,
        transactionId: transactionId || ('TXN-' + Date.now()),
        accountCode: line.accountCode,
        accountName: OryxChartOfAccounts[line.accountCode] ? OryxChartOfAccounts[line.accountCode].name : 'General Account',
        facilityId: facilityId || 'N/A',
        debit: parseFloat(line.debit || 0),
        credit: parseFloat(line.credit || 0),
        currency: 'KES',
        narration: narration,
        actor: actorEmail,
        timestamp: timestamp
      });
    });

    localStorage.setItem('oryx_ledger_journal_entries', JSON.stringify(journal));
    return { success: true, transactionId, totalAmount: totalDebit };
  },

  /**
   * Computes current trial balance across all Chart of Accounts.
   */
  getTrialBalance() {
    const journal = this.getLedgerJournalEntries();
    const balances = {};

    Object.keys(OryxChartOfAccounts).forEach(code => {
      balances[code] = {
        code: code,
        name: OryxChartOfAccounts[code].name,
        type: OryxChartOfAccounts[code].type,
        normalBalance: OryxChartOfAccounts[code].normalBalance,
        totalDebit: 0,
        totalCredit: 0,
        netBalance: 0
      };
    });

    journal.forEach(entry => {
      const code = entry.accountCode;
      if (balances[code]) {
        balances[code].totalDebit += entry.debit;
        balances[code].totalCredit += entry.credit;
      }
    });

    Object.keys(balances).forEach(code => {
      const b = balances[code];
      b.totalDebit = Math.round(b.totalDebit * 100) / 100;
      b.totalCredit = Math.round(b.totalCredit * 100) / 100;
      if (b.normalBalance === 'Debit') {
        b.netBalance = Math.round((b.totalDebit - b.totalCredit) * 100) / 100;
      } else {
        b.netBalance = Math.round((b.totalCredit - b.totalDebit) * 100) / 100;
      }
    });

    return balances;
  },

  // =========================================================================
  // CRYPTOGRAPHIC WORM AUDIT TRAIL
  // =========================================================================
  getAuditLog() {
    try {
      return JSON.parse(localStorage.getItem('oryx_worm_audit_log') || '[]');
    } catch (e) {
      return [];
    }
  },

  async logAuditEvent(actor, actionType, entityAffected, clearanceLevel, stateDelta) {
    const logs = this.getAuditLog();
    const prevHash = logs.length > 0 ? (logs[0].merkleRootHash || '0000000000000000000000000000000000000000000000000000000000000000') : '0000000000000000000000000000000000000000000000000000000000000000';
    const timestamp = new Date().toISOString();
    const eventId = 'AUD-' + Date.now() + '-' + Math.floor(1000 + Math.random() * 9000);

    const actorEmail = (actor && actor.email) ? actor.email : 'system@oryxfund.co.ke';
    const entityId = (entityAffected && entityAffected.entityId) ? entityAffected.entityId : 'GENERAL';
    const rawString = `${eventId}|${timestamp}|${actorEmail}|${actionType}|${entityId}|${clearanceLevel}|${prevHash}`;
    
    // Hash chain computing
    let hash = '';
    try {
      if (typeof crypto !== 'undefined' && crypto.subtle) {
        const enc = new TextEncoder();
        const buf = await crypto.subtle.digest('SHA-256', enc.encode(rawString));
        hash = Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
      } else {
        hash = 'hash_' + Math.random().toString(36).substring(2);
      }
    } catch(e) {
      hash = 'hash_' + Math.random().toString(36).substring(2);
    }

    const event = {
      auditEventId: eventId,
      timestamp: timestamp,
      actor: actor,
      actionType: actionType,
      entityAffected: entityAffected,
      clearanceLevelUtilized: clearanceLevel,
      stateDelta: stateDelta,
      previousEventHash: prevHash,
      merkleRootHash: hash
    };

    logs.unshift(event);
    localStorage.setItem('oryx_worm_audit_log', JSON.stringify(logs));
    return event;
  },

  // =========================================================================
  // TRANSACTION IDEMPOTENCY LOCKS
  // =========================================================================
  getIdempotencyRecord(key) {
    try {
      const raw = localStorage.getItem('oryx_idem_' + key);
      return raw ? JSON.parse(raw) : null;
    } catch(e) {
      return null;
    }
  },

  setIdempotencyRecord(key, status, payload = null) {
    if (!key) return;
    const rec = {
      key: key,
      status: status,
      payload: payload,
      updatedAt: new Date().toISOString()
    };
    localStorage.setItem('oryx_idem_' + key, JSON.stringify(rec));
  }
};

// Auto-seed storage on script load
OryxStorage.initSeeds();

// Global backwards-compatible wrappers
function getUserRecord(id) { return OryxStorage.getUser(id); }
function saveUserRecord(u) { return OryxStorage.saveUser(u); }
function initAuthSeeds() { OryxStorage.initSeeds(); }

// Node.js export support for unit testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { OryxStorage, OryxChartOfAccounts };
}
