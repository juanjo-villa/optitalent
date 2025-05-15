from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreateAdmin, EmployeeCreateUser, EmployeeUpdate
from app.models.role import RoleEnum

def create_employee(db: Session, payload: EmployeeCreateAdmin | EmployeeCreateUser, role: RoleEnum) -> Employee:
    new_employee = Employee(
        dni=payload.dni,
        first_name=payload.first_name,
        last_name=payload.last_name,
        address=payload.address,
        phone_number=payload.phone_number,
        email=payload.email,
        password=payload.password,
        role=role,
        id_position=payload.id_position
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db: Session, employee_id: int, payload: EmployeeUpdate) -> Employee | None:
    employee = get_employee_by_id(db, employee_id)
    if employee:
        employee.first_name = payload.first_name
        employee.last_name = payload.last_name
        employee.address = payload.address
        employee.phone_number = payload.phone_number
        employee.id_position = payload.id_position
        db.commit()
        db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int) -> bool:
    employee = get_employee_by_id(db, employee_id)
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False

def get_employee_by_email(db: Session, email: str) -> Employee | None:
    return db.query(Employee).filter(Employee.email == email).first()


def get_employee_by_id(db: Session, employee_id: int) -> Employee | None:
    return db.query(Employee).filter(Employee.id == employee_id).first()