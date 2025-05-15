from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.payroll_schema import PayrollCreate, PayrollUpdate, PayrollOut
from app.service import payroll_service
from app.security.roles import require_admin
from app.models.employee import Employee

router = APIRouter(prefix="/payrolls", tags=["Payrolls"])

@router.post("/", response_model=PayrollOut, status_code=201)
def create_payroll(payload: PayrollCreate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    return payroll_service.create_payroll_service(db, payload)

@router.put("/{payroll_id}", response_model=PayrollOut)
def update_payroll(payroll_id: int, payload: PayrollUpdate, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    updated = payroll_service.update_payroll_service(db, payroll_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Payroll not found")
    return updated

@router.delete("/{payroll_id}")
def delete_payroll(payroll_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    success = payroll_service.delete_payroll_service(db, payroll_id)
    if not success:
        raise HTTPException(status_code=404, detail="Payroll not found")
    return {"message": "Payroll deleted"}

@router.get("/{payroll_id}", response_model=PayrollOut)
def get_payroll(payroll_id: int, db: Session = Depends(get_db), _: Employee = Depends(require_admin)):
    payroll = payroll_service.get_payroll_service(db, payroll_id)
    if not payroll:
        raise HTTPException(status_code=404, detail="Payroll not found")
    return payroll