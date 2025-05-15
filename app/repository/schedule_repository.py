from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule_schema import ScheduleCreate, ScheduleUpdate

def create_schedule(db: Session, payload: ScheduleCreate) -> Schedule:
    new_schedule = Schedule(
        date=payload.date,
        start_time=payload.start_time,
        exit_time=payload.exit_time,
        total_hours=payload.total_hours,
        deducted_hours=payload.deducted_hours
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule

def update_schedule(db: Session, schedule_id: int, payload: ScheduleUpdate) -> Schedule | None:
    schedule = get_schedule_by_id(db, schedule_id)
    if schedule:
        schedule.date = payload.date
        schedule.start_time = payload.start_time
        schedule.exit_time = payload.exit_time
        schedule.total_hours = payload.total_hours
        schedule.deducted_hours = payload.deducted_hours
        db.commit()
        db.refresh(schedule)
    return schedule

def delete_schedule(db: Session, schedule_id: int) -> bool:
    schedule = get_schedule_by_id(db, schedule_id)
    if schedule:
        db.delete(schedule)
        db.commit()
        return True
    return False

def get_schedule_by_id(db: Session, schedule_id: int) -> Schedule | None:
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()

def get_all_schedules(db: Session) -> list[Schedule]:
    return db.query(Schedule).all()