from pydantic import BaseModel
from datetime import date, time

class ScheduleBase(BaseModel):
    date: date
    start_time: time
    exit_time: time
    total_hours: float
    deducted_hours: float 

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(ScheduleBase):
    pass

class ScheduleOut(ScheduleBase):
    id: int

    class Config:
        orm_mode = True