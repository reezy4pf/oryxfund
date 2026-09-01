"""
ORYX FUND — WORM AUDIT TRAIL UNIT TESTS (backend/tests/test_audit_worm.py)
Validates immutable audit logging, SHA-256 Merkle hash chaining, and tamper detection.
"""

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from backend.app.db.base import Base
from backend.app.services.audit_service import WormAuditService

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
async def test_worm_audit_logging_and_hash_chaining(async_db_session: AsyncSession):
    # Event 1: Sanction
    ev1 = await WormAuditService.log_audit_event(
        session=async_db_session,
        staff_email="dervinaziza9@gmail.com",
        staff_role="Lead Underwriter",
        action_type="FACILITY_SANCTIONED",
        entity_type="loan",
        entity_id="ACC-LOAN-2026-00001",
        state_delta={"pre_status": "Under Review", "post_status": "Sanctioned"},
        clearance_level=4
    )
    assert ev1.previous_event_hash == "0000000000000000000000000000000000000000000000000000000000000000"
    assert len(ev1.merkle_root_hash) == 64

    # Event 2: Disbursal
    ev2 = await WormAuditService.log_audit_event(
        session=async_db_session,
        staff_email="dervinaziza9@gmail.com",
        staff_role="Fund Manager",
        action_type="FACILITY_DISBURSED",
        entity_type="loan",
        entity_id="ACC-LOAN-2026-00001",
        state_delta={"disbursed_amount": 48200.00, "b2c_rail": "M-Pesa"},
        clearance_level=4
    )
    # Event 2's previous hash must match Event 1's Merkle root
    assert ev2.previous_event_hash == ev1.merkle_root_hash

    # Verify Mathematical Chain Integrity
    chain_status = await WormAuditService.verify_chain_integrity(async_db_session)
    assert chain_status["chain_valid"] is True
    assert chain_status["verified_events_count"] == 2
    assert chain_status["status"] == "CHAIN_INTEGRITY_VERIFIED_100%"

@pytest.mark.asyncio
async def test_worm_audit_tamper_detection(async_db_session: AsyncSession):
    # Log 2 events
    ev1 = await WormAuditService.log_audit_event(
        session=async_db_session,
        staff_email="staff@oryxfund.ke",
        staff_role="Underwriter",
        action_type="FACILITY_SANCTIONED",
        entity_type="loan",
        entity_id="LND-001",
        state_delta={"amount": 10000},
        clearance_level=3
    )

    ev2 = await WormAuditService.log_audit_event(
        session=async_db_session,
        staff_email="staff@oryxfund.ke",
        staff_role="Underwriter",
        action_type="FACILITY_DISBURSED",
        entity_type="loan",
        entity_id="LND-001",
        state_delta={"amount": 9600},
        clearance_level=4
    )

    # Intentionally corrupt Event 1's payload to simulate a database injection attack
    ev1.state_delta_json = '{"amount": 99999999}' # Tampered payload
    await async_db_session.commit()

    # Verify that the cryptographic hash chain detects the breach
    tamper_result = await WormAuditService.verify_chain_integrity(async_db_session)
    assert tamper_result["chain_valid"] is False
    assert tamper_result["status"] == "PAYLOAD_TAMPERING_DETECTED"
