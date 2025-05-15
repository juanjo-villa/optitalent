from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.employee_schedule_schema import EmployeeScheduleCreate, EmployeeScheduleOut
from app.service import employee_schedule_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/employee-schedules", tags=["EmployeeSchedule"])

# Only ADMINs can assign a schedule to an employee
@router.post("/", response_model=EmployeeScheduleOut)
def assign_schedule(
    payload: EmployeeScheduleCreate,
    db: Session = Depends(get_db),
    _: Employee = Depends(require_admin)
):
    return employee_schedule_service.create_assignment(db, payload)

# Retrieve all schedules assigned to a specific employee
@router.get("/by-employee/{employee_id}", response_model=list[EmployeeScheduleOut])
def get_schedules_by_employee(employee_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return employee_schedule_service.get_assignments_by_employee(db, employee_id)

# Retrieve all employees assigned to a specific schedule
@router.get("/by-schedule/{schedule_id}", response_model=list[EmployeeScheduleOut])
def get_employees_by_schedule(schedule_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return employee_schedule_service.get_assignments_by_schedule(db, schedule_id)

# Only ADMINs can remove a schedule assignment
@router.delete("/{assignment_id}")
def remove_assignment(
    assignment_id: int,
    db: Session = Depends(get_db),
    _: Employee = Depends(require_admin)
):
    success = employee_schedule_service.delete_assignment(db, assignment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"message": "Assignment removed successfully"}
