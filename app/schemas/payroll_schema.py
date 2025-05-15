from pydantic import BaseModel
from datetime import date
from typing import Optional

class PayrollBase(BaseModel):
    id_employee: int
    paymentDate: date
    amount: float
    status: str
    id_bonuses: Optional[int] = None
    id_hours_extra: Optional[int] = None
    id_deductions: Optional[int] = None

class PayrollCreate(PayrollBase):
    pass

class PayrollUpdate(PayrollBase):
    pass

class PayrollOut(PayrollBase):
    id: int
    class Config:
        orm_mode = True