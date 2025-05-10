from sqlalchemy import Column, Integer
from fastapi.db.database import Base

class IAAnalysis(Base):
    __tablename__ = "ia_analysis"
    id = Column(Integer, primary_key=True)
