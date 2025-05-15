from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.status_permission_schema import StatusPermissionCreate, StatusPermissionUpdate, StatusPermissionOut
from app.service import status_permission_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/status-permissions", tags=["StatusPermissions"])

@router.post("/", response_model=StatusPermissionOut, status_code=201)
def create_status_permission(payload: StatusPermissionCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return status_permission_service.create_status_permission_service(db, payload)

@router.put("/{permission_id}", response_model=StatusPermissionOut)
def update_status_permission(permission_id: int, payload: StatusPermissionUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = status_permission_service.update_status_permission_service(db, permission_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="StatusPermission not found")
    return updated

@router.delete("/{permission_id}")
def delete_status_permission(permission_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = status_permission_service.delete_status_permission_service(db, permission_id)
    if not success:
        raise HTTPException(status_code=404, detail="StatusPermission not found")
    return {"message": "StatusPermission deleted"}

@router.get("/{permission_id}", response_model=StatusPermissionOut)
def get_status_permission(permission_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    perm = status_permission_service.get_status_permission_service(db, permission_id)
    if not perm:
        raise HTTPException(status_code=404, detail="StatusPermission not found")
    return perm
