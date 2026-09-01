"""
ORYX FUND — IMMUTABLE WORM AUDIT TRAIL SERVICE (backend/app/services/audit_service.py)
Implements Write-Once-Read-Many (WORM) audit event logging with cryptographic SHA-256 hash chaining
and mathematical ledger integrity verification (CBK / ODPC / KDPA 2019 compliant).
"""

import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.ledger import WormAuditLog

GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

class WormAuditService:
    @classmethod
    def compute_event_hash(
        cls, 
        audit_event_id: str, 
        timestamp_str: str, 
        staff_email: str, 
        action_type: str, 
        entity_id: str, 
        clearance_level: int, 
        state_delta_json: str, 
        previous_event_hash: str
    ) -> str:
        """
        Computes deterministic SHA-256 Merkle hash for the audit event:
        H_i = SHA-256(event_id || timestamp || email || action || entity || level || delta || prev_hash)
        """
        raw_string = (
            f"{audit_event_id}|{timestamp_str}|{staff_email}|{action_type}|"
            f"{entity_id}|{clearance_level}|{state_delta_json}|{previous_event_hash}"
        )
        return hashlib.sha256(raw_string.encode("utf-8")).hexdigest()

    @classmethod
    async def log_audit_event(
        cls,
        session: AsyncSession,
        staff_email: str,
        staff_role: str,
        action_type: str,
        entity_type: str,
        entity_id: str,
        state_delta: Dict[str, Any],
        clearance_level: int = 4
    ) -> WormAuditLog:
        """
        Appends an immutable audit event to the WORM log, cryptographically chained to the previous record.
        """
        # 1. Fetch latest audit event to get previous hash
        stmt = select(WormAuditLog).order_by(WormAuditLog.timestamp.desc()).limit(1)
        res = await session.execute(stmt)
        latest_entry = res.scalar_one_or_none()

        prev_hash = latest_entry.merkle_root_hash if latest_entry else GENESIS_HASH

        # 2. Build new audit event
        import uuid
        event_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc)
        delta_str = json.dumps(state_delta, sort_keys=True)

        event_hash = cls.compute_event_hash(
            audit_event_id=event_id,
            timestamp_str=now.isoformat(),
            staff_email=staff_email,
            action_type=action_type,
            entity_id=entity_id,
            clearance_level=clearance_level,
            state_delta_json=delta_str,
            previous_event_hash=prev_hash
        )

        entry = WormAuditLog(
            audit_event_id=event_id,
            timestamp=now,
            staff_email=staff_email,
            staff_role=staff_role,
            action_type=action_type,
            entity_type=entity_type,
            entity_id=entity_id,
            clearance_level_utilized=clearance_level,
            state_delta_json=delta_str,
            previous_event_hash=prev_hash,
            merkle_root_hash=event_hash
        )

        session.add(entry)
        await session.commit()
        return entry

    @classmethod
    async def get_audit_trail(
        cls, 
        session: AsyncSession, 
        limit: int = 100
    ) -> List[WormAuditLog]:
        """Retrieves audit trail entries in reverse chronological order."""
        stmt = select(WormAuditLog).order_by(WormAuditLog.timestamp.desc()).limit(limit)
        res = await session.execute(stmt)
        return list(res.scalars().all())

    @classmethod
    async def verify_chain_integrity(cls, session: AsyncSession) -> Dict[str, Any]:
        """
        Mathematically verifies the entire cryptographic hash chain from Genesis.
        Returns validation status and verified block count.
        """
        stmt = select(WormAuditLog).order_by(WormAuditLog.timestamp.asc())
        res = await session.execute(stmt)
        entries = res.scalars().all()

        if not entries:
            return {
                "chain_valid": True,
                "verified_events_count": 0,
                "status": "GENESIS_EMPTY"
            }

        expected_prev_hash = GENESIS_HASH
        for idx, entry in enumerate(entries):
            if entry.previous_event_hash != expected_prev_hash:
                return {
                    "chain_valid": False,
                    "tampered_event_id": entry.audit_event_id,
                    "event_index": idx,
                    "status": "HASH_CHAIN_BROKEN_PREV_MISMATCH"
                }

            recalculated_hash = cls.compute_event_hash(
                audit_event_id=entry.audit_event_id,
                timestamp_str=entry.timestamp.isoformat(),
                staff_email=entry.staff_email,
                action_type=entry.action_type,
                entity_id=entry.entity_id,
                clearance_level=entry.clearance_level_utilized,
                state_delta_json=entry.state_delta_json,
                previous_event_hash=entry.previous_event_hash
            )

            if recalculated_hash != entry.merkle_root_hash:
                return {
                    "chain_valid": False,
                    "tampered_event_id": entry.audit_event_id,
                    "event_index": idx,
                    "status": "PAYLOAD_TAMPERING_DETECTED"
                }

            expected_prev_hash = entry.merkle_root_hash

        return {
            "chain_valid": True,
            "verified_events_count": len(entries),
            "latest_merkle_root": expected_prev_hash,
            "status": "CHAIN_INTEGRITY_VERIFIED_100%"
        }
