"""
ORYX FUND — LEDGER SCHEMAS (backend/app/schemas/ledger.py)
Pydantic validation schemas for double-entry journal transactions, Chart of Accounts, and Trial Balance.
"""

from decimal import Decimal
from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator

class JournalEntryLine(BaseModel):
    account_code: str = Field(..., min_length=4, max_length=16)
    debit: Decimal = Field(default=Decimal("0.0000"), ge=0)
    credit: Decimal = Field(default=Decimal("0.0000"), ge=0)

class PostJournalTransactionRequest(BaseModel):
    transaction_id: str = Field(..., min_length=4, max_length=64)
    narration: str = Field(..., min_length=5)
    facility_id: str = Field(default="N/A", max_length=32)
    booking_date: Optional[date] = Field(default_factory=date.today)
    actor: str = Field(default="system", max_length=128)
    lines: List[JournalEntryLine] = Field(..., min_length=2)

    @model_validator(mode="after")
    def validate_double_entry_balance(self):
        total_debit = sum(line.debit for line in self.lines)
        total_credit = sum(line.credit for line in self.lines)
        if total_debit != total_credit:
            raise ValueError(f"Double-entry balance mismatch: Debits ({total_debit}) != Credits ({total_credit})")
        return self

class JournalTransactionResponse(BaseModel):
    success: bool
    transaction_id: str
    total_debit: Decimal
    total_credit: Decimal
    lines_count: int
    timestamp: datetime

class TrialBalanceItem(BaseModel):
    account_code: str
    account_name: str
    category: str
    normal_balance: str
    total_debit: Decimal
    total_credit: Decimal
    net_balance: Decimal

class TrialBalanceResponse(BaseModel):
    is_balanced: bool
    total_debit: Decimal
    total_credit: Decimal
    accounts: List[TrialBalanceItem]
    timestamp: datetime
