from sqlalchemy.orm import Session
from app.models.payroll import Payroll
from app.schemas.payroll_schema import PayrollCreate, PayrollUpdate

def create_payroll(db: Session, payload: PayrollCreate) -> Payroll:
    payroll = Payroll(**payload.dict())
    db.add(payroll)
    db.commit()
    db.refresh(payroll)
    return payroll

def update_payroll(db: Session, payroll_id: int, payload: PayrollUpdate) -> Payroll | None:
    payroll = get_payroll_by_id(db, payroll_id)
    if payroll:
        for key, value in payload.dict().items():
            setattr(payroll, key, value)
        db.commit()
        db.refresh(payroll)
    return payroll

def delete_payroll(db: Session, payroll_id: int) -> bool:
    payroll = get_payroll_by_id(db, payroll_id)
    if payroll:
        db.delete(payroll)
        db.commit()
        return True
    return False

def get_payroll_by_id(db: Session, payroll_id: int) -> Payroll | None:
    return db.query(Payroll).filter(Payroll.id == payroll_id).first()