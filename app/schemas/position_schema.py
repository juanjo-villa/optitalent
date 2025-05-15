from pydantic import BaseModel

class PositionBase(BaseModel):
    name: str
    description: str
    salary: float

class PositionCreate(PositionBase):
    pass

class PositionUpdate(PositionBase):
    pass

class PositionOut(PositionBase):
    id: int

    class Config:
        orm_mode = True

