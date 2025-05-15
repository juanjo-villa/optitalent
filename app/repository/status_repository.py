from sqlalchemy.orm import Session
from app.models.status import Status
from app.schemas.status_schema import StatusCreate, StatusUpdate

def create_status(db: Session, payload: StatusCreate) -> Status:
    status = Status(**payload.dict())
    db.add(status)
    db.commit()
    db.refresh(status)
    return status

def update_status(db: Session, status_id: int, payload: StatusUpdate) -> Status | None:
    status = get_status_by_id(db, status_id)
    if status:
        for key, value in payload.dict().items():
            setattr(status, key, value)
        db.commit()
        db.refresh(status)
    return status

def delete_status(db: Session, status_id: int) -> bool:
    status = get_status_by_id(db, status_id)
    if status:
        db.delete(status)
        db.commit()
        return True
    return False

def get_status_by_id(db: Session, status_id: int) -> Status | None:
    return db.query(Status).filter(Status.id == status_id).first()