from sqlalchemy import Column, Integer, Date, Time, Float
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    startTime = Column(Time)
    exitTime = Column(Time)
    totalHours = Column(Float)
    deductedHours = Column(Float)

    employee_schedules = relationship("EmployeeSchedule", back_populates="schedule")
