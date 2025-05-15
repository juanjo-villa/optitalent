from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.status_schema import StatusCreate, StatusUpdate, StatusOut
from app.service import status_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/statuses", tags=["Statuses"])

@router.post("/", response_model=StatusOut, status_code=201)
def create_status(payload: StatusCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return status_service.create_status_service(db, payload)

@router.put("/{status_id}", response_model=StatusOut)
def update_status(status_id: int, payload: StatusUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = status_service.update_status_service(db, status_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Status not found")
    return updated

@router.delete("/{status_id}")
def delete_status(status_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = status_service.delete_status_service(db, status_id)
    if not success:
        raise HTTPException(status_code=404, detail="Status not found")
    return {"message": "Status deleted"}

@router.get("/{status_id}", response_model=StatusOut)
def get_status(status_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    status = status_service.get_status_service(db, status_id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status