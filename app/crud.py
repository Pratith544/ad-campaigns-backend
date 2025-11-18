from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from . import models

def get_campaigns(db: Session, status: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[models.Campaign]:
    q = db.query(models.Campaign)
    if status:
        q = q.filter(models.Campaign.status == status)
    return q.order_by(models.Campaign.id).offset(offset).limit(limit).all()

def create_campaign(db: Session, name: str, status: str, clicks: int, cost: float, impressions: int) -> models.Campaign:
    campaign = models.Campaign(
        name=name,
        status=status,
        clicks=clicks,
        cost=cost,
        impressions=impressions
    )
    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    return campaign