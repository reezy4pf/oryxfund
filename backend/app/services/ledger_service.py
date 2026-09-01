"""
ORYX FUND — DOUBLE-ENTRY LEDGER SERVICE (backend/app/services/ledger_service.py)
Implements atomic double-entry journal postings, trial balance generation, and ledger auditing.
"""

from decimal import Decimal
from datetime import datetime, date, timezone
from typing import List, Dict, Any, Optional
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.ledger import CoreLedgerEntry, ChartOfAccount
from backend.app.schemas.ledger import PostJournalTransactionRequest, TrialBalanceItem, TrialBalanceResponse

DEFAULT_CHART_OF_ACCOUNTS = [
    {"account_code": "10100", "account_name": "M-Pesa B2C Utility Float", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "10200", "account_name": "M-Pesa C2B Collections Float", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "10300", "account_name": "Commercial Bank Settlement Float", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "12000", "account_name": "Loans Receivable – Principal", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "12100", "account_name": "Interest Receivable – Accrued", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "12200", "account_name": "Late Penalty Receivable", "category": "Asset", "normal_balance": "Debit"},
    {"account_code": "12900", "account_name": "Allowance for Credit Losses (ECL)", "category": "Contra-Asset", "normal_balance": "Credit"},
    {"account_code": "20100", "account_name": "Borrower Unallocated Repayments (Suspense)", "category": "Liability", "normal_balance": "Credit"},
    {"account_code": "20200", "account_name": "Excise Duty Payable (KRA)", "category": "Liability", "normal_balance": "Credit"},
    {"account_code": "21000", "account_name": "Senior Debt / Institutional LP Capital", "category": "Liability", "normal_balance": "Credit"},
    {"account_code": "30100", "account_name": "Retained Earnings", "category": "Equity", "normal_balance": "Credit"},
    {"account_code": "40100", "account_name": "Interest Income", "category": "Revenue", "normal_balance": "Credit"},
    {"account_code": "40200", "account_name": "Processing Fee Income", "category": "Revenue", "normal_balance": "Credit"},
    {"account_code": "40300", "account_name": "Penalty & Late Fee Revenue", "category": "Revenue", "normal_balance": "Credit"},
    {"account_code": "50100", "account_name": "Provision Expense for Bad Debts", "category": "Expense", "normal_balance": "Debit"},
    {"account_code": "50200", "account_name": "Payment Gateway & Rail Expenses", "category": "Expense", "normal_balance": "Debit"},
    {"account_code": "50300", "account_name": "Principal Loan Write-Off", "category": "Expense", "normal_balance": "Debit"},
]

class LedgerService:
    @classmethod
    async def seed_chart_of_accounts(cls, session: AsyncSession):
        """Initializes default Chart of Accounts if empty."""
        result = await session.execute(select(func.count(ChartOfAccount.account_code)))
        count = result.scalar() or 0
        if count == 0:
            for item in DEFAULT_CHART_OF_ACCOUNTS:
                account = ChartOfAccount(
                    account_code=item["account_code"],
                    account_name=item["account_name"],
                    category=item["category"],
                    normal_balance=item["normal_balance"]
                )
                session.add(account)
            await session.commit()

    @classmethod
    async def post_journal_transaction(
        cls, 
        session: AsyncSession, 
        req: PostJournalTransactionRequest
    ) -> Dict[str, Any]:
        """
        Posts balanced double-entry lines within an atomic ACID transaction.
        Enforces: Total Debits == Total Credits.
        """
        total_debit = sum(line.debit for line in req.lines)
        total_credit = sum(line.credit for line in req.lines)

        if total_debit != total_credit:
            raise ValueError(f"Double-entry balance mismatch: Debits ({total_debit}) != Credits ({total_credit})")

        now = datetime.now(timezone.utc)
        b_date = req.booking_date or date.today()

        entries = []
        for line in req.lines:
            entry = CoreLedgerEntry(
                transaction_id=req.transaction_id,
                account_code=line.account_code,
                facility_id=req.facility_id,
                debit_amount=line.debit,
                credit_amount=line.credit,
                currency="KES",
                booking_date=b_date,
                value_timestamp=now,
                narration=req.narration,
                actor=req.actor
            )
            session.add(entry)
            entries.append(entry)

        await session.commit()

        return {
            "success": True,
            "transaction_id": req.transaction_id,
            "total_debit": total_debit,
            "total_credit": total_credit,
            "lines_count": len(entries),
            "timestamp": now
        }

    @classmethod
    async def get_trial_balance(cls, session: AsyncSession) -> TrialBalanceResponse:
        """
        Computes the complete Trial Balance across all accounts.
        """
        await cls.seed_chart_of_accounts(session)
        
        # Load all accounts
        coa_res = await session.execute(select(ChartOfAccount).order_by(ChartOfAccount.account_code))
        accounts = coa_res.scalars().all()

        # Query aggregated debits and credits per account
        stmt = select(
            CoreLedgerEntry.account_code,
            func.coalesce(func.sum(CoreLedgerEntry.debit_amount), Decimal("0.0000")).label("sum_debit"),
            func.coalesce(func.sum(CoreLedgerEntry.credit_amount), Decimal("0.0000")).label("sum_credit")
        ).group_by(CoreLedgerEntry.account_code)
        
        res = await session.execute(stmt)
        sums_map = {row.account_code: (row.sum_debit, row.sum_credit) for row in res.all()}

        items: List[TrialBalanceItem] = []
        grand_debit = Decimal("0.0000")
        grand_credit = Decimal("0.0000")

        for acc in accounts:
            debit, credit = sums_map.get(acc.account_code, (Decimal("0.0000"), Decimal("0.0000")))
            grand_debit += debit
            grand_credit += credit

            if acc.normal_balance == "Debit":
                net = debit - credit
            else:
                net = credit - debit

            items.append(TrialBalanceItem(
                account_code=acc.account_code,
                account_name=acc.account_name,
                category=acc.category,
                normal_balance=acc.normal_balance,
                total_debit=debit,
                total_credit=credit,
                net_balance=net
            ))

        return TrialBalanceResponse(
            is_balanced=(grand_debit == grand_credit),
            total_debit=grand_debit,
            total_credit=grand_credit,
            accounts=items,
            timestamp=datetime.now(timezone.utc)
        )

    @classmethod
    async def get_ledger_entries(
        cls, 
        session: AsyncSession, 
        facility_id: Optional[str] = None,
        account_code: Optional[str] = None,
        limit: int = 100
    ) -> List[CoreLedgerEntry]:
        """Retrieves ledger entries matching optional filters."""
        stmt = select(CoreLedgerEntry).order_by(CoreLedgerEntry.value_timestamp.desc()).limit(limit)
        if facility_id:
            stmt = stmt.where(CoreLedgerEntry.facility_id == facility_id)
        if account_code:
            stmt = stmt.where(CoreLedgerEntry.account_code == account_code)
        
        result = await session.execute(stmt)
        return list(result.scalars().all())
