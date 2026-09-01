"""
ORYX FUND — LEDGER & CORE ENTITY MODELS (backend/app/models/ledger.py)
Declarative SQLAlchemy models for double-entry financial ledger, chart of accounts,
loan facilities, credit applications, WORM audit trails, and idempotency records.
"""

import uuid
from datetime import datetime, date, timezone
from decimal import Decimal
from typing import Optional
from sqlalchemy import String, Numeric, Date, DateTime, Boolean, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.db.base import Base

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class CoreLedgerEntry(Base):
    """
    Immutable Double-Entry Ledger Journal Entry Table.
    Target PostgreSQL Partitioning: PARTITION BY RANGE (booking_date).
    """
    __tablename__ = "core_ledger_entries"

    entry_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    transaction_id: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    account_code: Mapped[str] = mapped_column(String(16), index=True, nullable=False)
    facility_id: Mapped[str] = mapped_column(String(32), index=True, nullable=False, default="N/A")
    debit_amount: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, default=Decimal("0.0000"))
    credit_amount: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False, default=Decimal("0.0000"))
    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="KES")
    booking_date: Mapped[date] = mapped_column(Date, primary_key=True, default=date.today)
    value_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    narration: Mapped[str] = mapped_column(Text, nullable=False)
    actor: Mapped[str] = mapped_column(String(128), nullable=False, default="system")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)

class ChartOfAccount(Base):
    """
    Master Chart of Accounts (COA) catalog.
    """
    __tablename__ = "chart_of_accounts"

    account_code: Mapped[str] = mapped_column(String(16), primary_key=True)
    account_name: Mapped[str] = mapped_column(String(128), nullable=False)
    category: Mapped[str] = mapped_column(String(32), nullable=False) # Asset, Liability, Equity, Revenue, Expense
    normal_balance: Mapped[str] = mapped_column(String(8), nullable=False) # Debit or Credit
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

class LoanFacility(Base):
    """
    Loan account and servicing ledger model.
    """
    __tablename__ = "loan_facilities"

    loan_id: Mapped[str] = mapped_column(String(32), primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(128), nullable=False)
    product_name: Mapped[str] = mapped_column(String(128), nullable=False)
    sanctioned_principal: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    disbursed_principal: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    outstanding_balance: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    monthly_installment: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    annual_rate_percent: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("14.00"))
    tenure_months: Mapped[int] = mapped_column(Integer, nullable=False, default=12)
    days_past_due: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    cbk_provision_tier: Mapped[str] = mapped_column(String(32), default="Normal (Performing)", nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="Active", nullable=False) # Active, Closed, Restructured, Written_Off
    disbursed_date: Mapped[date] = mapped_column(Date, default=date.today)
    next_due_date: Mapped[date] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)

class LoanApplication(Base):
    """
    Digital credit application pipeline model.
    """
    __tablename__ = "loan_applications"

    application_id: Mapped[str] = mapped_column(String(32), primary_key=True)
    applicant_name: Mapped[str] = mapped_column(String(128), nullable=False)
    national_id: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    product_name: Mapped[str] = mapped_column(String(128), nullable=False)
    requested_amount: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    stated_monthly_income: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    tenure_months: Mapped[int] = mapped_column(Integer, nullable=False, default=12)
    crb_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    dti_ratio_percent: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2), nullable=True)
    decision: Mapped[str] = mapped_column(String(64), default="Under Review", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)

class WormAuditLog(Base):
    """
    Immutable Regulatory WORM Audit Trail.
    """
    __tablename__ = "worm_audit_logs"

    audit_event_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False, index=True)
    staff_email: Mapped[str] = mapped_column(String(128), nullable=False)
    staff_role: Mapped[str] = mapped_column(String(64), nullable=False)
    action_type: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    entity_type: Mapped[str] = mapped_column(String(32), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(64), nullable=False)
    clearance_level_utilized: Mapped[int] = mapped_column(Integer, nullable=False, default=4)
    state_delta_json: Mapped[str] = mapped_column(Text, nullable=False)
    previous_event_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    merkle_root_hash: Mapped[str] = mapped_column(String(64), nullable=False, index=True)

class IdempotencyRecord(Base):
    """
    Distributed transaction deduplication and lock records.
    """
    __tablename__ = "idempotency_records"

    idempotency_key: Mapped[str] = mapped_column(String(64), primary_key=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False) # PROCESSING, SUCCESS, FAILED
    response_payload_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)
