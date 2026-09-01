"""
ORYX FUND — CORE BACKEND APPLICATION (backend/app/main.py)
FastAPI production application entry point for the Oryx Fund digital lending platform.
"""

import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
from backend.app.db.session import engine
from backend.app.db.base import Base
from backend.app.core.telemetry import TelemetryEngine
from backend.app.api.v1 import calculator, ledger, mpesa, crb, auth, audit, telemetry

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup database connections on shutdown
    await engine.dispose()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Institutional Digital Lending Fund & Underwriting Core (Central Bank of Kenya DCP Regulations 2022 Compliant)",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Metrics Middleware
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time) * 1000
    TelemetryEngine.record_request(
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration_ms=duration_ms
    )
    return response

# Mount API Routers
app.include_router(calculator.router, prefix=settings.API_V1_STR)
app.include_router(ledger.router, prefix=settings.API_V1_STR)
app.include_router(mpesa.router, prefix=settings.API_V1_STR)
app.include_router(crb.router, prefix=settings.API_V1_STR)
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(audit.router, prefix=settings.API_V1_STR)
app.include_router(telemetry.router, prefix=settings.API_V1_STR)

@app.get("/metrics", tags=["Prometheus Scraping"])
async def prometheus_metrics():
    """Exposes Prometheus text formatted metric counters and gauges."""
    return Response(
        content=TelemetryEngine.generate_prometheus_metrics_text(),
        media_type="text/plain"
    )

@app.get("/health", tags=["System Health"])
async def health_check():
    """System health & readiness check."""
    return {
        "status": "ONLINE",
        "platform": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "cbk_dcp_compliance": "ACTIVE",
        "ledger_engine": "DOUBLE_ENTRY_ACID",
        "payment_gateway": "SAFARICOM_DARAJA_2.0",
        "bureau_pipeline": "CRB_REGULATIONS_2020",
        "security_iam": "OAUTH2_PKCE_WEBAUTHN_FIDO2",
        "cryptography": "FIELD_LEVEL_ENVELOPE_AES_256_GCM",
        "audit_storage": "IMMUTABLE_WORM_HASH_CHAINED",
        "observability": "OPENTELEMETRY_PROMETHEUS_GRAFANA"
    }

@app.get("/", tags=["System Root"])
async def root():
    return {
        "message": "Oryx Fund Core Lending API Online",
        "docs_url": "/docs",
        "metrics_url": "/metrics",
        "health_check": "/health"
    }
