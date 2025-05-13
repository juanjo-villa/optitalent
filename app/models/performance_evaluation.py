from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class PerformanceEvaluation(Base):
    __tablename__ = "performance_evaluation"
    id = Column(Integer, primary_key=True)
    id_employee = Column(Integer, ForeignKey("employee.id"))
    date = Column(Date)
    score = Column(Integer)
    comments = Column(String)

    employee = relationship("Employee", back_populates="performance_evaluations")
