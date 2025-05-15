from sqlalchemy.orm import Session
from app.schemas.count_employee_schedule_schema import (
    CountEmployeeScheduleCreate,
    CountEmployeeScheduleUpdate
)
from app.models.count_employee_schedule import CountEmployeeSchedule
from app.repository import count_employee_schedule_repository

def create_service(db: Session, payload: CountEmployeeScheduleCreate) -> CountEmployeeSchedule:
    obj = CountEmployeeSchedule(**payload.dict())
    return count_employee_schedule_repository.create(db, obj)

def get_by_id_service(db: Session, count_id: int):
    return count_employee_schedule_repository.get_by_id(db, count_id)

def get_all_service(db: Session):
    return count_employee_schedule_repository.get_all(db)

def update_service(db: Session, count_id: int, payload: CountEmployeeScheduleUpdate):
    db_obj = count_employee_schedule_repository.get_by_id(db, count_id)
    if not db_obj:
        return None
    return count_employee_schedule_repository.update(db, db_obj, payload.dict())

def delete_service(db: Session, count_id: int) -> bool:
    db_obj = count_employee_schedule_repository.get_by_id(db, count_id)
    if not db_obj:
        return False
    count_employee_schedule_repository.delete(db, db_obj)
    return True
