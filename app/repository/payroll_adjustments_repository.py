from sqlalchemy.orm import Session
from app.models.payroll_adjustments import PayrollAdjustments
from app.schemas.payroll_adjustments_schema import PayrollAdjustmentsCreate, PayrollAdjustmentsUpdate

def create_payroll_adjustment(db: Session, payload: PayrollAdjustmentsCreate) -> PayrollAdjustments:
    adj = PayrollAdjustments(**payload.dict())
    db.add(adj)
    db.commit()
    db.refresh(adj)
    return adj

def update_payroll_adjustment(db: Session, adjustment_id: int, payload: PayrollAdjustmentsUpdate) -> PayrollAdjustments | None:
    adj = get_payroll_adjustment_by_id(db, adjustment_id)
    if adj:
        for key, value in payload.dict().items():
            setattr(adj, key, value)
        db.commit()
        db.refresh(adj)
    return adj

def delete_payroll_adjustment(db: Session, adjustment_id: int) -> bool:
    adj = get_payroll_adjustment_by_id(db, adjustment_id)
    if adj:
        db.delete(adj)
        db.commit()
        return True
    return False

def get_payroll_adjustment_by_id(db: Session, adjustment_id: int) -> PayrollAdjustments | None:
    return db.query(PayrollAdjustments).filter(PayrollAdjustments.id == adjustment_id).first()