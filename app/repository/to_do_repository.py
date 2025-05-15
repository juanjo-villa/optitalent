from sqlalchemy.orm import Session
from app.models.to_do import ToDo
from app.schemas.to_do_schema import ToDoCreate, ToDoUpdate

def create_to_do(db: Session, payload: ToDoCreate) -> ToDo:
    task = ToDo()
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_to_do(db: Session, task_id: int, payload: ToDoUpdate) -> ToDo | None:
    task = get_to_do_by_id(db, task_id)
    if task:
        db.commit()
        db.refresh(task)
    return task

def delete_to_do(db: Session, task_id: int) -> bool:
    task = get_to_do_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False

def get_to_do_by_id(db: Session, task_id: int) -> ToDo | None:
    return db.query(ToDo).filter(ToDo.id == task_id).first()