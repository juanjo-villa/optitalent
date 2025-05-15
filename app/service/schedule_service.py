from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.repository import schedule_repository
from app.schemas.schedule_schema import ScheduleCreate, ScheduleUpdate

def create_schedule_service(db: Session, payload: ScheduleCreate) -> Schedule:
    return schedule_repository.create_schedule(db, payload)

def get_schedule_by_id_service(db: Session, schedule_id: int) -> Schedule | None:
    return schedule_repository.get_schedule_by_id(db, schedule_id)

def get_all_schedules_service(db: Session) -> list[Schedule]:
    return schedule_repository.get_all_schedules(db)

def update_schedule_service(db: Session, schedule_id: int, payload: ScheduleUpdate) -> Schedule | None:
    return schedule_repository.update_schedule(db, schedule_id, payload)

def delete_schedule_service(db: Session, schedule_id: int) -> bool:
    return schedule_repository.delete_schedule(db, schedule_id)

