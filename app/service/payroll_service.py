from sqlalchemy.orm import Session
from app.repository import payroll_repository
from app.schemas.payroll_schema import PayrollCreate, PayrollUpdate
from app.models.payroll import Payroll

def create_payroll_service(db: Session, payload: PayrollCreate) -> Payroll:
    return payroll_repository.create_payroll(db, payload)

def update_payroll_service(db: Session, payroll_id: int, payload: PayrollUpdate) -> Payroll | None:
    return payroll_repository.update_payroll(db, payroll_id, payload)

def delete_payroll_service(db: Session, payroll_id: int) -> bool:
    return payroll_repository.delete_payroll(db, payroll_id)

def get_payroll_service(db: Session, payroll_id: int) -> Payroll | None:
    return payroll_repository.get_payroll_by_id(db, payroll_id)