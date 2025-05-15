from sqlalchemy.orm import Session
from app.models.position import Position
from app.schemas.position_schema import PositionCreate, PositionUpdate

def create_position(db: Session, payload: PositionCreate) -> Position:
    new_position = Position(
        name=payload.name,
        description=payload.description,
        salary=payload.salary
    )
    db.add(new_position)
    db.commit()
    db.refresh(new_position)
    return new_position

def update_position(db: Session, position_id: int, payload: PositionUpdate) -> Position | None:
    position = get_position_by_id(db, position_id)
    if position:
        position.name = payload.name
        position.description = payload.description
        position.salary = payload.salary
        db.commit()
        db.refresh(position)
    return position

def delete_position(db: Session, position_id: int) -> bool:
    position = get_position_by_id(db, position_id)
    if position:
        db.delete(position)
        db.commit()
        return True
    return False

def get_position_by_id(db: Session, position_id: int) -> Position | None:
    return db.query(Position).filter(Position.id == position_id).first()
