from pydantic import BaseModel
from datetime import date
from typing import Optional

class PerformanceEvaluationBase(BaseModel):
    id_employee: int
    date: date
    score: int
    comments: Optional[str] = None

class PerformanceEvaluationCreate(PerformanceEvaluationBase):
    pass

class PerformanceEvaluationUpdate(PerformanceEvaluationBase):
    pass

class PerformanceEvaluationOut(PerformanceEvaluationBase):
    id: int
    class Config:
        orm_mode = True