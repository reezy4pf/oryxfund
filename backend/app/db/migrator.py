"""
ORYX FUND — ASYNC DATABASE SCHEMA MIGRATOR & INTEGRITY ENGINE (backend/app/db/migrator.py)
Programmatic migration runner that initializes declarative models and verifies schema consistency.
"""

from typing import Dict, Any, List
from sqlalchemy import text, inspect
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from backend.app.db.base import Base
import backend.app.models.ledger # Register all declarative models

class DatabaseMigrator:
    @classmethod
    async def run_schema_migration(cls, engine: AsyncEngine) -> Dict[str, Any]:
        """Creates all registered database schema tables if not existing."""
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        tables = list(Base.metadata.tables.keys())
        return {
            "status": "MIGRATIONS_APPLIED_SUCCESSFULLY",
            "tables_registered": tables,
            "table_count": len(tables)
        }

    @classmethod
    async def verify_schema_integrity(cls, engine: AsyncEngine) -> Dict[str, Any]:
        """Inspects and verifies that all 6 critical tables exist and are accessible."""
        required_tables = [
            "chart_of_accounts",
            "core_ledger_entries",
            "loan_facilities",
            "loan_applications",
            "worm_audit_logs",
            "idempotency_records"
        ]
        
        async with engine.connect() as conn:
            missing_tables = []
            for t in required_tables:
                try:
                    await conn.execute(text(f"SELECT 1 FROM {t} LIMIT 1"))
                except Exception:
                    missing_tables.append(t)

        return {
            "schema_valid": len(missing_tables) == 0,
            "missing_tables": missing_tables,
            "required_tables_count": len(required_tables)
        }
