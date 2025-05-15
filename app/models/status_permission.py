from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class StatusPermission(Base):
    __tablename__ = "status_permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    statuses = relationship("Status", back_populates="status_permission")