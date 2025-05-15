from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.employee_schema import (
    EmployeeCreateAdmin,
    EmployeeCreateUser,
    EmployeeUpdate,
    EmployeeOut,
)
from app.models.role import RoleEnum
from app.service import employee_service
from app.security.roles import require_admin
from app.models.employee import Employee


router = APIRouter(prefix="/employees", tags=["Employees"])

# Create first ADMIN
@router.post("/admin/create", response_model=EmployeeOut)
def create_admin(payload: EmployeeCreateAdmin, db: Session = Depends(get_db)):
    existing_employee = employee_service.get_employee_by_email_service(db, payload.email)
    if existing_employee:
        raise HTTPException(status_code=400, detail="Admin already exists")
    return employee_service.create_employee_service(db, payload, payload.role)

# Register new USER
@router.post("/register", response_model=EmployeeOut)
def register_user(payload: EmployeeCreateUser, db: Session = Depends(get_db)):
    existing_employee = employee_service.get_employee_by_email_service(db, payload.email)
    if existing_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    return employee_service.create_employee_service(db, payload, RoleEnum.USER)

# Get employee by ID
@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    employee = employee_service.get_employee_by_id_service(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update employee data
@router.put("/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: int, payload: EmployeeUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated_employee = employee_service.update_employee_service(db, employee_id, payload)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

# Delete employee
@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    deleted = employee_service.delete_employee_service(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
