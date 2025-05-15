from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    description = Column(String(255), nullable=True)
    paid = Column(Float, nullable=False)

    id_employee = Column(Integer, ForeignKey("employees.id"), nullable=False)
    id_statusPermission = Column(Integer, ForeignKey("status_permissions.id"), nullable=False)

    employee = relationship("Employee", back_populates="statuses")
    status_permission = relationship("StatusPermission", back_populates="statuses")