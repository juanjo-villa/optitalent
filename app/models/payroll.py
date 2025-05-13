from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class Payroll(Base):
    __tablename__ = "payroll"
    id = Column(Integer, primary_key=True)
    id_employee = Column(Integer, ForeignKey("employee.id"))
    paymentDate = Column(Date)
    amount = Column(Float)
    status = Column(String)
    id_bonus = Column(Integer)
    id_hours_extra = Column(Integer)
    id_deductions = Column(Integer)

    employee = relationship("Employee", back_populates="payrolls")
    adjustments = relationship("PayrollAdjustments", back_populates="payroll")
