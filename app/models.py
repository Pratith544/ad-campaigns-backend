from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    clicks = Column(Integer)
    cost = Column(Float)
    impressions = Column(Integer)
    image_url = Column(String, nullable=False)
