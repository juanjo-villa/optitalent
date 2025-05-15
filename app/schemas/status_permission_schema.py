from pydantic import BaseModel
from typing import Optional

class StatusPermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class StatusPermissionCreate(StatusPermissionBase):
    pass

class StatusPermissionUpdate(StatusPermissionBase):
    pass

class StatusPermissionOut(StatusPermissionBase):
    id: int
    class Config:
        orm_mode = True