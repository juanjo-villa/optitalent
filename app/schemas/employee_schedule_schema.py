from pydantic import BaseModel

class EmployeeScheduleCreate(BaseModel):
    id_employee: int
    id_schedule: int

class EmployeeScheduleOut(BaseModel):
    id: int
    id_employee: int
    id_schedule: int

    class Config:
        orm_mode = True