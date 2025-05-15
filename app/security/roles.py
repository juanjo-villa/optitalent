from fastapi import Depends, HTTPException, status
from app.models.employee import Employee
from app.security.auth import get_current_user

def require_admin(current_user: Employee = Depends(get_current_user)) -> Employee:
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user
