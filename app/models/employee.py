from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.role import RoleEnum


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    role = Column(SqlEnum(RoleEnum), nullable=False, default=RoleEnum.USER)

    id_position = Column(Integer, ForeignKey("position.id"), nullable=False)
    position = relationship("Position", backref="employees")