from sqlalchemy import Column, Integer
from app.db.base import Base

class ToDo(Base):
    __tablename__ = "to_do"

    id = Column(Integer, primary_key=True, index=True)