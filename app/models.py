from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False, index=True)  # 'Active' or 'Paused'
    clicks = Column(Integer, nullable=False, default=0)
    cost = Column(Float, nullable=False, default=0.0)
    impressions = Column(Integer, nullable=False, default=0)