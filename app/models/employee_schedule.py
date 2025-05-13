from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class EmployeeSchedule(Base):
    __tablename__ = "employee_schedule"
    id = Column(Integer, primary_key=True)
    id_employee = Column(Integer, ForeignKey("employee.id"))
    id_schedule = Column(Integer, ForeignKey("schedule.id"))

    employee = relationship("Employee", back_populates="schedules")
    schedule = relationship("Schedule", back_populates="employee_schedules")
    count_schedule = relationship("CountEmployeeSchedule", back_populates="employee_schedule")
