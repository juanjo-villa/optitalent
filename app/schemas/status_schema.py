from pydantic import BaseModel
from datetime import date

class StatusBase(BaseModel):
    type: str
    startDate: date
    endDate: date
    description: str
    paid: float
    id_employee: int
    id_statusPermission: int

class StatusCreate(StatusBase):
    pass

class StatusUpdate(StatusBase):
    pass

class StatusOut(StatusBase):
    id: int
    class Config:
        orm_mode = True