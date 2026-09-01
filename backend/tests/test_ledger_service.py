"""
ORYX FUND — LEDGER SERVICE UNIT TESTS (backend/tests/test_ledger_service.py)
Validates double-entry accounting journal postings, zero-sum debit/credit invariance, and trial balance generation.
"""

from decimal import Decimal
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from backend.app.db.base import Base
from backend.app.services.ledger_service import LedgerService
from backend.app.schemas.ledger import PostJournalTransactionRequest, JournalEntryLine

# Use an in-memory SQLite database for unit test isolation
TEST_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_db_session():
    test_engine = create_async_engine(TEST_DB_URL, echo=False)
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    test_session_maker = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)
    async with test_session_maker() as session:
        yield session
    
    await test_engine.dispose()

@pytest.mark.asyncio
async def test_post_balanced_journal_transaction(async_db_session: AsyncSession):
    # Balanced Disbursal Transaction of KES 50,000
    req = PostJournalTransactionRequest(
        transaction_id="TXN-TEST-DISB-001",
        narration="Disbursal of loan ACC-LOAN-2026-00001 with 20% KRA Excise Duty",
        facility_id="ACC-LOAN-2026-00001",
        actor="dervinaziza9@gmail.com",
        lines=[
            JournalEntryLine(account_code="12000", debit=Decimal("50000.00"), credit=Decimal("0.00")),
            JournalEntryLine(account_code="10100", debit=Decimal("0.00"), credit=Decimal("48200.00")),
            JournalEntryLine(account_code="40200", debit=Decimal("0.00"), credit=Decimal("1500.00")),
            JournalEntryLine(account_code="20200", debit=Decimal("0.00"), credit=Decimal("300.00")),
        ]
    )

    result = await LedgerService.post_journal_transaction(async_db_session, req)
    assert result["success"] is True
    assert result["transaction_id"] == "TXN-TEST-DISB-001"
    assert result["total_debit"] == Decimal("50000.00")
    assert result["total_credit"] == Decimal("50000.00")
    assert result["lines_count"] == 4

@pytest.mark.asyncio
async def test_trial_balance_generation(async_db_session: AsyncSession):
    # 1. Post Disbursal
    req1 = PostJournalTransactionRequest(
        transaction_id="TXN-DISB-001",
        narration="Disbursement",
        facility_id="LND-001",
        lines=[
            JournalEntryLine(account_code="12000", debit=Decimal("50000.00"), credit=Decimal("0.00")),
            JournalEntryLine(account_code="10100", debit=Decimal("0.00"), credit=Decimal("48200.00")),
            JournalEntryLine(account_code="40200", debit=Decimal("0.00"), credit=Decimal("1500.00")),
            JournalEntryLine(account_code="20200", debit=Decimal("0.00"), credit=Decimal("300.00")),
        ]
    )
    await LedgerService.post_journal_transaction(async_db_session, req1)

    # 2. Post Repayment of KES 10,000 (Principal 8,500 + Interest 1,500)
    req2 = PostJournalTransactionRequest(
        transaction_id="TXN-REP-001",
        narration="M-Pesa C2B Repayment",
        facility_id="LND-001",
        lines=[
            JournalEntryLine(account_code="10200", debit=Decimal("10000.00"), credit=Decimal("0.00")),
            JournalEntryLine(account_code="12000", debit=Decimal("0.00"), credit=Decimal("8500.00")),
            JournalEntryLine(account_code="40100", debit=Decimal("0.00"), credit=Decimal("1500.00")),
        ]
    )
    await LedgerService.post_journal_transaction(async_db_session, req2)

    # 3. Query Trial Balance
    tb = await LedgerService.get_trial_balance(async_db_session)
    assert tb.is_balanced is True
    assert tb.total_debit == Decimal("60000.00")
    assert tb.total_credit == Decimal("60000.00")

    # Inspect individual account balances
    acc_map = {a.account_code: a for a in tb.accounts}
    assert acc_map["12000"].net_balance == Decimal("41500.00") # 50,000 - 8,500
    assert acc_map["10200"].net_balance == Decimal("10000.00") # +10,000 collections
    assert acc_map["40100"].net_balance == Decimal("1500.00")  # +1,500 interest yield
