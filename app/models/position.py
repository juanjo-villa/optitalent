from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique = True)
    description = Column(String(255), nullable=False)
    salary = Column(Float, nullable=False)
