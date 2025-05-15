from pydantic import BaseModel

class ToDoBase(BaseModel):
    pass

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    pass

class ToDoOut(ToDoBase):
    id: int
    class Config:
        orm_mode = True