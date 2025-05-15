from pydantic import BaseModel
from datetime import date

class CountEmployeeScheduleBase(BaseModel):
    id_employee_schedule: int
    work_date: date
    work_hours: float

class CountEmployeeScheduleCreate(CountEmployeeScheduleBase):
    pass

class CountEmployeeScheduleUpdate(CountEmployeeScheduleBase):
    pass

class CountEmployeeScheduleOut(CountEmployeeScheduleBase):
    id: int

    class Config:
        orm_mode = True
