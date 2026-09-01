"""initial_ledger_and_facilities

Revision ID: 0001_initial_ledger_and_facilities
Revises: 
Create Date: 2026-09-01 12:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '0001_initial_ledger_and_facilities'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # 1. Chart of Accounts
    op.create_table(
        'chart_of_accounts',
        sa.Column('code', sa.String(length=10), nullable=False),
        sa.Column('name', sa.String(length=150), nullable=False),
        sa.Column('account_type', sa.String(length=30), nullable=False),
        sa.Column('normal_balance', sa.String(length=10), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.PrimaryKeyConstraint('code')
    )

    # 2. Core Ledger Entries
    op.create_table(
        'core_ledger_entries',
        sa.Column('entry_id', sa.String(length=40), nullable=False),
        sa.Column('transaction_id', sa.String(length=50), nullable=False),
        sa.Column('account_code', sa.String(length=10), nullable=False),
        sa.Column('facility_id', sa.String(length=50), nullable=True),
        sa.Column('booking_date', sa.Date(), nullable=False),
        sa.Column('debit', sa.Numeric(precision=18, scale=2), nullable=False, default=0.00),
        sa.Column('credit', sa.Numeric(precision=18, scale=2), nullable=False, default=0.00),
        sa.Column('currency', sa.String(length=3), nullable=False, default='KES'),
        sa.Column('narration', sa.Text(), nullable=False),
        sa.Column('actor_email', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('entry_id', 'booking_date')
    )

    # 3. Loan Facilities
    op.create_table(
        'loan_facilities',
        sa.Column('facility_id', sa.String(length=50), nullable=False),
        sa.Column('borrower_id', sa.String(length=50), nullable=False),
        sa.Column('borrower_name', sa.String(length=255), nullable=False),
        sa.Column('borrower_phone', sa.String(length=30), nullable=False),
        sa.Column('product_type', sa.String(length=100), nullable=False),
        sa.Column('principal', sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column('annual_interest_rate', sa.Numeric(precision=6, scale=4), nullable=False),
        sa.Column('tenure_months', sa.Integer(), nullable=False),
        sa.Column('monthly_installment', sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column('outstanding_balance', sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column('days_past_due', sa.Integer(), nullable=False, default=0),
        sa.Column('cbk_classification', sa.String(length=50), nullable=False, default='Normal (Performing)'),
        sa.Column('ifrs9_stage', sa.String(length=20), nullable=False, default='Stage 1'),
        sa.Column('status', sa.String(length=30), nullable=False, default='ACTIVE'),
        sa.Column('disbursed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('facility_id')
    )

    # 4. Loan Applications
    op.create_table(
        'loan_applications',
        sa.Column('application_id', sa.String(length=50), nullable=False),
        sa.Column('borrower_id', sa.String(length=50), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('encrypted_national_id', sa.Text(), nullable=False),
        sa.Column('encrypted_phone', sa.Text(), nullable=False),
        sa.Column('encrypted_stated_income', sa.Text(), nullable=False),
        sa.Column('product_name', sa.String(length=100), nullable=False),
        sa.Column('requested_amount', sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column('tenure_months', sa.Integer(), nullable=False),
        sa.Column('crb_score', sa.Integer(), nullable=True),
        sa.Column('dti_ratio', sa.Numeric(precision=6, scale=2), nullable=True),
        sa.Column('status', sa.String(length=40), nullable=False, default='UNDERWRITING_REVIEW'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('application_id')
    )

    # 5. WORM Audit Logs
    op.create_table(
        'worm_audit_logs',
        sa.Column('event_id', sa.String(length=50), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
        sa.Column('actor_email', sa.String(length=255), nullable=False),
        sa.Column('actor_role', sa.String(length=100), nullable=False),
        sa.Column('action_type', sa.String(length=100), nullable=False),
        sa.Column('entity_type', sa.String(length=50), nullable=False),
        sa.Column('entity_id', sa.String(length=100), nullable=False),
        sa.Column('clearance_level', sa.Integer(), nullable=False),
        sa.Column('state_delta_json', sa.Text(), nullable=False),
        sa.Column('previous_event_hash', sa.String(length=64), nullable=False),
        sa.Column('merkle_root_hash', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('event_id')
    )

    # 6. Idempotency Records
    op.create_table(
        'idempotency_records',
        sa.Column('idempotency_key', sa.String(length=128), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('response_payload', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('idempotency_key')
    )

def downgrade() -> None:
    op.drop_table('idempotency_records')
    op.drop_table('worm_audit_logs')
    op.drop_table('loan_applications')
    op.drop_table('loan_facilities')
    op.drop_table('core_ledger_entries')
    op.drop_table('chart_of_accounts')
