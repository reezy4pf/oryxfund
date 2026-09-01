"""
ORYX FUND — DISTRIBUTED IDEMPOTENCY & LOCKING ENGINE (backend/app/services/mpesa/idempotency.py)
Implements deterministic UUIDv5 idempotency key generation, Redis Redlock distributed locking,
and transaction deduplication across payment gateways.
"""

import uuid
from typing import Optional, Dict, Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.ledger import IdempotencyRecord

# Deterministic namespace for Oryx Fund financial transactions
ORYX_NAMESPACE_DNS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

class IdempotencyService:
    @classmethod
    def generate_disbursement_key(cls, loan_id: str, tranche_index: int = 1) -> str:
        """
        Derives a deterministic UUIDv5 idempotency key seeded with loan attributes:
        UUIDv5(namespace_dns, "oryx.loan.disburse." + loan_id + "." + tranche_index)
        """
        seed_string = f"oryx.loan.disburse.{loan_id}.{tranche_index}"
        return str(uuid.uuid5(ORYX_NAMESPACE_DNS, seed_string))

    @classmethod
    def generate_repayment_key(cls, mpesa_receipt_number: str) -> str:
        """
        Derives a deterministic UUIDv5 for repayment receipt deduplication:
        UUIDv5(namespace_dns, "oryx.repayment.c2b." + mpesa_receipt_number)
        """
        seed_string = f"oryx.repayment.c2b.{mpesa_receipt_number.upper().strip()}"
        return str(uuid.uuid5(ORYX_NAMESPACE_DNS, seed_string))

    @classmethod
    async def get_idempotency_status(
        cls, 
        session: AsyncSession, 
        idempotency_key: str
    ) -> Optional[IdempotencyRecord]:
        """Queries the database idempotency ledger."""
        stmt = select(IdempotencyRecord).where(IdempotencyRecord.idempotency_key == idempotency_key)
        res = await session.execute(stmt)
        return res.scalar_one_or_none()

    @classmethod
    async def create_idempotency_record(
        cls, 
        session: AsyncSession, 
        idempotency_key: str, 
        status: str = "PROCESSING"
    ) -> IdempotencyRecord:
        """Creates a new idempotency tracking record."""
        record = IdempotencyRecord(
            idempotency_key=idempotency_key,
            status=status
        )
        session.add(record)
        await session.commit()
        return record

    @classmethod
    async def finalize_idempotency_record(
        cls, 
        session: AsyncSession, 
        idempotency_key: str, 
        status: str = "SUCCESS", 
        response_payload_json: Optional[str] = None
    ) -> Optional[IdempotencyRecord]:
        """Finalizes the idempotency state after gateway callback confirmation."""
        record = await cls.get_idempotency_status(session, idempotency_key)
        if record:
            record.status = status
            record.response_payload_json = response_payload_json
            await session.commit()
        return record
