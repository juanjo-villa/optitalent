from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class EmployeeSchedule(Base):
    __tablename__ = "employee_schedules"

    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, ForeignKey("employees.id"), nullable=False)
    id_schedule = Column(Integer, ForeignKey("schedules.id"), nullable=False)

    employee = relationship("Employee", backref="schedules")
    schedule = relationship("Schedule", backref="employees")