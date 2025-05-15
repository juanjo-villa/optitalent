from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.payroll_adjustments_schema import PayrollAdjustmentsCreate, PayrollAdjustmentsUpdate, PayrollAdjustmentsOut
from app.service import payroll_adjustments_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/payroll-adjustments", tags=["PayrollAdjustments"])

@router.post("/", response_model=PayrollAdjustmentsOut, status_code=201)
def create_payroll_adjustment(payload: PayrollAdjustmentsCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return payroll_adjustments_service.create_payroll_adjustment_service(db, payload)

@router.put("/{adjustment_id}", response_model=PayrollAdjustmentsOut)
def update_payroll_adjustment(adjustment_id: int, payload: PayrollAdjustmentsUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = payroll_adjustments_service.update_payroll_adjustment_service(db, adjustment_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Adjustment not found")
    return updated

@router.delete("/{adjustment_id}")
def delete_payroll_adjustment(adjustment_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = payroll_adjustments_service.delete_payroll_adjustment_service(db, adjustment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Adjustment not found")
    return {"message": "Adjustment deleted"}

@router.get("/{adjustment_id}", response_model=PayrollAdjustmentsOut)
def get_payroll_adjustment(adjustment_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    adj = payroll_adjustments_service.get_payroll_adjustment_service(db, adjustment_id)
    if not adj:
        raise HTTPException(status_code=404, detail="Adjustment not found")
    return adj