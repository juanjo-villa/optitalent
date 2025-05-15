from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.schedule_schema import (
    ScheduleCreate,
    ScheduleUpdate,
    ScheduleOut
)
from app.service import schedule_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/schedules", tags=["Schedules"])

# 🔹 Create a new schedule
@router.post("/", response_model=ScheduleOut, status_code=201)
def create_schedule(payload: ScheduleCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return schedule_service.create_schedule_service(db, payload)

# 🔹 Update a schedule by ID
@router.put("/{schedule_id}", response_model=ScheduleOut)
def update_schedule(schedule_id: int, payload: ScheduleUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = schedule_service.update_schedule_service(db, schedule_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated

# 🔹 Delete a schedule by ID
@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    deleted = schedule_service.delete_schedule_service(db, schedule_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"message": "Schedule deleted successfully"}

# 🔹 List all schedules
@router.get("/", response_model=list[ScheduleOut])
def list_schedules(db: Session = Depends(get_db)):
    return schedule_service.get_all_schedules_service(db)

# 🔹 Get a schedule by ID
@router.get("/{schedule_id}", response_model=ScheduleOut)
def get_schedule(schedule_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    schedule = schedule_service.get_schedule_by_id_service(db, schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule
