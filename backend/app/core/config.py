"""
ORYX FUND — CORE CONFIGURATION (backend/app/core/config.py)
Centralized environment configuration, regulatory parameters, and secret management.
"""

from typing import List
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = ConfigDict(case_sensitive=True, env_file=".env", extra="ignore")

    PROJECT_NAME: str = "Oryx Fund Core Platform"
    VERSION: str = "2.0.0-production"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "production"

    # Database & Pooling Configuration (PostgreSQL 16+ via PgBouncer)
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "oryx_admin"
    POSTGRES_PASSWORD: str = "OryxSecure2026_Key"
    POSTGRES_DB: str = "oryx_fund_ledger"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = "sqlite+aiosqlite:///./oryx_fund.db" # Default fallback for local testing, overridden by env

    # Redis Cache & Distributed Locking (Redlock)
    REDIS_URL: str = "redis://localhost:6379/0"

    # JWT & Authentication Configuration
    JWT_SECRET_KEY: str = "oryx_fund_2026_asymmetric_ecdsa_ed25519_key_signature"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 240  # 4 Hours session TTL

    # Administrative Root Credentials (Overridable via environment variables)
    ADMIN_DEFAULT_EMAIL: str = "dervinaziza9@gmail.com"
    ADMIN_DEFAULT_PASSWORD_HASH: str = "91521ad19aee4d15e8ed916c75354a4411e6a5c43703ddb048411c41b67732c7" # Oryx2026

    # Central Bank of Kenya (CBK) Statutory Lending Parameters
    STATUTORY_EXCISE_DUTY_RATE: float = 0.20  # 20% KRA Excise on fees
    DEFAULT_APPRAISAL_FEE_RATE: float = 0.02  # 2.0% Facility Processing Fee
    DEFAULT_LATE_PENALTY_RATE: float = 0.02   # 2.0% / month

    # CORS Allowed Origins
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:3000",
        "https://oryxfund.ke",
        "https://desk.oryxfund.ke"
    ]

settings = Settings()
