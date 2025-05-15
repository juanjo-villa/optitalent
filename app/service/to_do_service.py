from sqlalchemy.orm import Session
from app.repository import to_do_repository
from app.schemas.to_do_schema import ToDoCreate, ToDoUpdate
from app.models.to_do import ToDo

def create_to_do_service(db: Session, payload: ToDoCreate) -> ToDo:
    return to_do_repository.create_to_do(db, payload)

def update_to_do_service(db: Session, task_id: int, payload: ToDoUpdate) -> ToDo | None:
    return to_do_repository.update_to_do(db, task_id, payload)

def delete_to_do_service(db: Session, task_id: int) -> bool:
    return to_do_repository.delete_to_do(db, task_id)

def get_to_do_service(db: Session, task_id: int) -> ToDo | None:
    return to_do_repository.get_to_do_by_id(db, task_id)