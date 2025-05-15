from sqlalchemy.orm import Session
from app.repository import employee_schedule_repository
from app.schemas.employee_schedule_schema import EmployeeScheduleCreate
from app.models.employee_schedule import EmployeeSchedule

def create_assignment(db: Session, payload: EmployeeScheduleCreate) -> EmployeeSchedule:
    return employee_schedule_repository.create_employee_schedule(db, payload)

def get_assignments_by_employee(db: Session, employee_id: int) -> list[EmployeeSchedule]:
    return employee_schedule_repository.get_by_employee_id(db, employee_id)

def get_assignments_by_schedule(db: Session, schedule_id: int) -> list[EmployeeSchedule]:
    return employee_schedule_repository.get_by_schedule_id(db, schedule_id)

def delete_assignment(db: Session, assignment_id: int) -> bool:
    return employee_schedule_repository.delete_employee_schedule(db, assignment_id)
