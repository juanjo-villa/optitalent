from sqlalchemy import Column, Integer, Float, ForeignKey, String
from app.db.base import Base

class PayrollAdjustments(Base):
    __tablename__ = "payroll_adjustments"

    id = Column(Integer, primary_key=True, index=True)
    id_payroll = Column(Integer, ForeignKey("payrolls.id"), nullable=False)
    type = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    amount = Column(Float, nullable=False)