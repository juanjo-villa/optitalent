from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class Position(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    salary = Column(Float)

    employees = relationship("Employee", back_populates="position")