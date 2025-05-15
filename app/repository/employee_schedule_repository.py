from sqlalchemy.orm import Session
from app.models.employee_schedule import EmployeeSchedule
from app.schemas.employee_schedule_schema import EmployeeScheduleCreate

def create_employee_schedule(db: Session, payload: EmployeeScheduleCreate) -> EmployeeSchedule:
    assignment = EmployeeSchedule(
        id_employee=payload.id_employee,
        id_schedule=payload.id_schedule
    )
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment

def get_by_employee_id(db: Session, employee_id: int) -> list[EmployeeSchedule]:
    return db.query(EmployeeSchedule).filter(EmployeeSchedule.id_employee == employee_id).all()

def get_by_schedule_id(db: Session, schedule_id: int) -> list[EmployeeSchedule]:
    return db.query(EmployeeSchedule).filter(EmployeeSchedule.id_schedule == schedule_id).all()

def delete_employee_schedule(db: Session, assignment_id: int) -> bool:
    record = db.query(EmployeeSchedule).filter(EmployeeSchedule.id == assignment_id).first()
    if record:
        db.delete(record)
        db.commit()
        return True
    return False
