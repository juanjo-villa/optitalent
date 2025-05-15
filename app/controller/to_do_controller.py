from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.to_do_schema import ToDoCreate, ToDoUpdate, ToDoOut
from app.service import to_do_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/to-do", tags=["ToDo"])

@router.post("/", response_model=ToDoOut, status_code=201)
def create_to_do(payload: ToDoCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return to_do_service.create_to_do_service(db, payload)

@router.put("/{task_id}", response_model=ToDoOut)
def update_to_do(task_id: int, payload: ToDoUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = to_do_service.update_to_do_service(db, task_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="ToDo task not found")
    return updated

@router.delete("/{task_id}")
def delete_to_do(task_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = to_do_service.delete_to_do_service(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="ToDo task not found")
    return {"message": "ToDo task deleted"}

@router.get("/{task_id}", response_model=ToDoOut)
def get_to_do(task_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    task = to_do_service.get_to_do_service(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="ToDo task not found")
    return task
