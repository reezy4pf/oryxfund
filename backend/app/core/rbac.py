"""
ORYX FUND — ROLE-BASED ACCESS CONTROL (RBAC) (backend/app/core/rbac.py)
Enforces granular institutional clearance levels (Level 1 through Level 5).
"""

from typing import Dict, Any, Callable
from fastapi import HTTPException, status, Depends
from backend.app.core.auth import get_current_user

def require_clearance(min_level: int) -> Callable:
    """
    FastAPI dependency factory enforcing minimum organizational clearance level:
    - Level 1: Loan Officer
    - Level 2: Junior Underwriter
    - Level 3: Senior Underwriter
    - Level 4: Fund Manager / CSO
    - Level 5: Compliance / Internal Audit
    """
    async def clearance_guard(current_user: Dict[str, Any] = Depends(get_current_user)):
        user_level = current_user.get("clearance_level", 1)
        if user_level < min_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient clearance: Action requires Level {min_level}, user holds Level {user_level}."
            )
        return current_user

    return clearance_guard

require_clearance_level = require_clearance
