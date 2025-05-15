from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Payroll(Base):
    __tablename__ = "payrolls"

    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, ForeignKey("employees.id"), nullable=False)
    paymentDate = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    id_bonuses = Column(Integer, nullable=True)
    id_hours_extra = Column(Integer, nullable=True)
    id_deductions = Column(Integer, nullable=True)

    employee = relationship("Employee", back_populates="payrolls")