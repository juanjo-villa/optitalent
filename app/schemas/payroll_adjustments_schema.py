from pydantic import BaseModel
from typing import Optional

class PayrollAdjustmentsBase(BaseModel):
    id_payroll: int
    type: str
    description: Optional[str] = None
    amount: float

class PayrollAdjustmentsCreate(PayrollAdjustmentsBase):
    pass

class PayrollAdjustmentsUpdate(PayrollAdjustmentsBase):
    pass

class PayrollAdjustmentsOut(PayrollAdjustmentsBase):
    id: int
    class Config:
        orm_mode = True