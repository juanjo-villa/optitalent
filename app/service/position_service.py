from sqlalchemy.orm import Session
from app.repository import position_repository
from app.models.position import Position
from app.schemas.position_schema import PositionCreate, PositionUpdate

def create_position_service(db: Session, payload: PositionCreate) -> Position:
    return position_repository.create_position(db, payload)

def update_position_service(db: Session, position_id: int, payload: PositionUpdate) -> Position | None:
    return position_repository.update_position(db, position_id, payload)

def delete_position_service(db: Session, position_id: int) -> bool:
    return position_repository.delete_position(db, position_id)

def get_position_service(db: Session, position_id: int) -> Position | None:
    return position_repository.get_position_by_id(db, position_id)