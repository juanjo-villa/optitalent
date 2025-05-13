from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class PayrollAdjustments(Base):
    __tablename__ = "payroll_adjustments"
    id = Column(Integer, primary_key=True)
    id_payroll = Column(Integer, ForeignKey("payroll.id"))
    type = Column(String)
    description = Column(String)
    amount = Column(Float)

    payroll = relationship("Payroll", back_populates="adjustments")
