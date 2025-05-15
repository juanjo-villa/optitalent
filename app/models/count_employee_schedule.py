from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from app.db.base import Base

class CountEmployeeSchedule(Base):
    __tablename__ = "count_employee_schedule"

    id = Column(Integer, primary_key=True, index=True)
    id_employee_schedule = Column(Integer, ForeignKey("employee_schedules.id"), nullable=False)
    work_date = Column(Date, nullable=False)
    work_hours = Column(Float, nullable=False)
