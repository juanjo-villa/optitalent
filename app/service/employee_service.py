from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.models.role import RoleEnum
from app.repository import employee_repository
from app.schemas.employee_schema import EmployeeCreateAdmin, EmployeeCreateUser, EmployeeUpdate

def create_employee_service(
    db: Session, payload: EmployeeCreateAdmin | EmployeeCreateUser, role: RoleEnum
) -> Employee:
    return employee_repository.create_employee(db, payload, role)

def get_employee_by_email_service(db: Session, email: str) -> Employee | None:
    return employee_repository.get_employee_by_email(db, email)

def get_employee_by_id_service(db: Session, employee_id: int) -> Employee | None:
    return employee_repository.get_employee_by_id(db, employee_id)

def update_employee_service(db: Session, employee_id: int, payload: EmployeeUpdate) -> Employee | None:
    return employee_repository.update_employee(db, employee_id, payload)

def delete_employee_service(db: Session, employee_id: int) -> bool:
    return employee_repository.delete_employee(db, employee_id)

