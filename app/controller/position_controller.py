from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.position_schema import PositionCreate, PositionUpdate, PositionOut
from app.service import position_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/positions", tags=["Positions"])

@router.post("/", response_model=PositionOut, status_code=201)
def create_position(payload: PositionCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return position_service.create_position_service(db, payload)

@router.put("/{position_id}", response_model=PositionOut)
def update_position(position_id: int, payload: PositionUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = position_service.update_position_service(db, position_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Position not found")
    return updated

@router.delete("/{position_id}")
def delete_position(position_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = position_service.delete_position_service(db, position_id)
    if not success:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"message": "Position deleted"}

@router.get("/{position_id}", response_model=PositionOut)
def get_position(position_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    position = position_service.get_position_service(db, position_id)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return position
