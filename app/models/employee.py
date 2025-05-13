from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from fastapi.db.database import Base

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    dni = Column(Integer)
    name = Column(String)
    lastName = Column(String)
    address = Column(String)
    email = Column(String)
    phone = Column(Integer)
    password = Column(String)
    company = Column(String)
    id_position = Column(Integer, ForeignKey("position.id"))
    id_company = Column(Integer)

    position = relationship("Position", back_populates="employees")
    schedules = relationship("EmployeeSchedule", back_populates="employee")
    statuses = relationship("Status", back_populates="employee")
    payrolls = relationship("Payroll", back_populates="employee")
    performance_evaluations = relationship("PerformanceEvaluation", back_populates="employee")
