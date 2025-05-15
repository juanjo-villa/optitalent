from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.count_employee_schedule_schema import (
    CountEmployeeScheduleCreate,
    CountEmployeeScheduleUpdate,
    CountEmployeeScheduleOut
)
from app.service import count_employee_schedule_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/count-employee-schedules", tags=["CountEmployeeSchedule"])

@router.post("/", response_model=CountEmployeeScheduleOut)
def create(payload: CountEmployeeScheduleCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return count_employee_schedule_service.create_service(db, payload)

@router.get("/{count_id}", response_model=CountEmployeeScheduleOut)
def get_by_id(count_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    data = count_employee_schedule_service.get_by_id_service(db, count_id)
    if not data:
        raise HTTPException(status_code=404, detail="Entry not found")
    return data

@router.get("/", response_model=list[CountEmployeeScheduleOut])
def get_all(db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return count_employee_schedule_service.get_all_service(db)

@router.put("/{count_id}", response_model=CountEmployeeScheduleOut)
def update(count_id: int, payload: CountEmployeeScheduleUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = count_employee_schedule_service.update_service(db, count_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Entry not found")
    return updated

@router.delete("/{count_id}")
def delete(count_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = count_employee_schedule_service.delete_service(db, count_id)
    if not success:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"message": "Deleted successfully"}
