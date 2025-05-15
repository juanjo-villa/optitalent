from sqlalchemy.orm import Session
from app.repository import payroll_adjustments_repository
from app.schemas.payroll_adjustments_schema import PayrollAdjustmentsCreate, PayrollAdjustmentsUpdate
from app.models.payroll_adjustments import PayrollAdjustments

def create_payroll_adjustment_service(db: Session, payload: PayrollAdjustmentsCreate) -> PayrollAdjustments:
    return payroll_adjustments_repository.create_payroll_adjustment(db, payload)

def update_payroll_adjustment_service(db: Session, adjustment_id: int, payload: PayrollAdjustmentsUpdate) -> PayrollAdjustments | None:
    return payroll_adjustments_repository.update_payroll_adjustment(db, adjustment_id, payload)

def delete_payroll_adjustment_service(db: Session, adjustment_id: int) -> bool:
    return payroll_adjustments_repository.delete_payroll_adjustment(db, adjustment_id)

def get_payroll_adjustment_service(db: Session, adjustment_id: int) -> PayrollAdjustments | None:
    return payroll_adjustments_repository.get_payroll_adjustment_by_id(db, adjustment_id)