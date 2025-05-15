from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class PerformanceEvaluation(Base):
    __tablename__ = "performance_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, ForeignKey("employees.id"), nullable=False)
    date = Column(Date, nullable=False)
    score = Column(Integer, nullable=False)
    comments = Column(String(255), nullable=True)

    employee = relationship("Employee", back_populates="performance_evaluations")
