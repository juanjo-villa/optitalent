from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    startDate = Column(Date)
    endDate = Column(Date)
    description = Column(String)
    paid = Column(Float)
    id_employee = Column(Integer, ForeignKey("employee.id"))
    id_statusPermission = Column(Integer, ForeignKey("status_permission.id"))

    employee = relationship("Employee", back_populates="statuses")
    status_permission = relationship("StatusPermission", back_populates="statuses")
