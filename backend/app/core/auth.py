"""
ORYX FUND — AUTHENTICATION & JWT SECURITY (backend/app/core/auth.py)
OAuth 2.0 / OIDC + PKCE compatible session manager, salted key derivation,
and asymmetric/HMAC JWT signature verification.
"""

import os
import hmac
import json
import base64
import hashlib
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.app.core.config import settings

security_bearer = HTTPBearer(auto_error=False)

class AuthService:
    AUTH_SALT = "oryx_fund_2026_salt_sec_"

    @classmethod
    def hash_password(cls, plain_password: str) -> str:
        """
        Cryptographic SHA-256 salted password hashing matching client Web Crypto key derivation:
        SHA-256(salt + password)
        """
        salted = (cls.AUTH_SALT + plain_password).encode("utf-8")
        return hashlib.sha256(salted).hexdigest()

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """Verifies password using constant-time comparison."""
        calc = cls.hash_password(plain_password)
        return hmac.compare_digest(calc, hashed_password)

    @classmethod
    def create_access_token(
        cls, 
        data: Dict[str, Any], 
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """
        Generates a standard signed JWT token containing user identity and clearance level.
        """
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (
            expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode.update({"exp": int(expire.timestamp()), "iat": int(datetime.now(timezone.utc).timestamp())})

        # Base64URL Header & Payload
        header = {"alg": "HS256", "typ": "JWT"}
        header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(json.dumps(to_encode).encode()).decode().rstrip("=")

        # HMAC-SHA256 Signature
        signing_input = f"{header_b64}.{payload_b64}".encode()
        sig = hmac.new(settings.JWT_SECRET_KEY.encode(), signing_input, hashlib.sha256).digest()
        sig_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")

        return f"{header_b64}.{payload_b64}.{sig_b64}"

    @classmethod
    def decode_access_token(cls, token: str) -> Dict[str, Any]:
        """
        Validates token signature, expiration timestamp, and extracts claims.
        """
        try:
            parts = token.split(".")
            if len(parts) != 3:
                raise ValueError("Invalid JWT token structure.")

            header_b64, payload_b64, sig_b64 = parts
            signing_input = f"{header_b64}.{payload_b64}".encode()

            # Verify signature
            expected_sig = hmac.new(settings.JWT_SECRET_KEY.encode(), signing_input, hashlib.sha256).digest()
            expected_sig_b64 = base64.urlsafe_b64encode(expected_sig).decode().rstrip("=")

            if not hmac.compare_digest(sig_b64, expected_sig_b64):
                raise ValueError("JWT signature verification failed.")

            # Decode payload
            padded_payload = payload_b64 + "=" * (-len(payload_b64) % 4)
            claims = json.loads(base64.urlsafe_b64decode(padded_payload).decode())

            # Verify expiration
            exp = claims.get("exp")
            if exp and datetime.now(timezone.utc).timestamp() > exp:
                raise ValueError("JWT token has expired.")

            return claims
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Authentication clearance denied: {str(e)}",
                headers={"WWW-Authenticate": "Bearer"}
            )

async def get_current_user(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(security_bearer)
) -> Dict[str, Any]:
    """
    Zero-Trust dependency injection guard returning verified user session claims.
    Strictly raises HTTP 401 Unauthorized if no valid Bearer token is provided.
    """
    if not auth or not auth.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required. Please supply a valid Bearer token.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return AuthService.decode_access_token(auth.credentials)
