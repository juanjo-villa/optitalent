from sqlalchemy.orm import Session
from app.repository import status_repository
from app.schemas.status_schema import StatusCreate, StatusUpdate
from app.models.status import Status

def create_status_service(db: Session, payload: StatusCreate) -> Status:
    return status_repository.create_status(db, payload)

def update_status_service(db: Session, status_id: int, payload: StatusUpdate) -> Status | None:
    return status_repository.update_status(db, status_id, payload)

def delete_status_service(db: Session, status_id: int) -> bool:
    return status_repository.delete_status(db, status_id)

def get_status_service(db: Session, status_id: int) -> Status | None:
    return status_repository.get_status_by_id(db, status_id)