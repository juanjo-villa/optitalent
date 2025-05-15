from sqlalchemy.orm import Session
from app.models.count_employee_schedule import CountEmployeeSchedule

def create(db: Session, payload: CountEmployeeSchedule) -> CountEmployeeSchedule:
    db.add(payload)
    db.commit()
    db.refresh(payload)
    return payload

def get_by_id(db: Session, count_id: int):
    return db.query(CountEmployeeSchedule).filter(CountEmployeeSchedule.id == count_id).first()

def get_all(db: Session):
    return db.query(CountEmployeeSchedule).all()

def update(db: Session, db_obj: CountEmployeeSchedule, updates: dict):
    for key, value in updates.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, db_obj: CountEmployeeSchedule):
    db.delete(db_obj)
    db.commit()
