from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class CountEmployeeSchedule(Base):
    __tablename__ = "count_employee_schedule"
    id = Column(Integer, primary_key=True)
    id_employee_schedule = Column(Integer, ForeignKey("employee_schedule.id"))
    work_date = Column(Date)
    work_hours = Column(Float)

    employee_schedule = relationship("EmployeeSchedule", back_populates="count_schedule")
