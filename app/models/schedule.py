from sqlalchemy import Column, Integer, Date, Time, Float
from app.db.base import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    exit_time = Column(Time, nullable=False)
    total_hours = Column(Float, nullable=False)
    deducted_hours = Column(Float, nullable=False)
