from pydantic import BaseModel, EmailStr
from app.models.role import RoleEnum

class EmployeeBase(BaseModel):
    dni: int
    first_name: str
    last_name: str
    address: str | None = None
    phone_number: str | None = None
    email: EmailStr
    password: str
    id_position: int


class EmployeeCreateAdmin(EmployeeBase):
    role: RoleEnum

class EmployeeCreateUser(EmployeeBase):
    pass 

class EmployeeUpdate(BaseModel):
    first_name: str
    last_name: str
    address: str | None = None
    phone_number: str | None = None
    id_position: int


class EmployeeOut(BaseModel):
    id: int
    dni: int
    first_name: str
    last_name: str
    address: str | None
    phone_number: str | None
    email: EmailStr
    role: RoleEnum
    id_position: int

    class Config:
        orm_mode = True