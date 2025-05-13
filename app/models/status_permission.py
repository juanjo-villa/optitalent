from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class StatusPermission(Base):
    __tablename__ = "status_permission"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    statuses = relationship("Status", back_populates="status_permission")