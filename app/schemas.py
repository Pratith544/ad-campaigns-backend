from pydantic import BaseModel, ConfigDict

class CampaignBase(BaseModel):
    name: str
    status: str
    clicks: int
    cost: float
    impressions: int
    image_url: str

class Campaign(CampaignBase):
    id: int

    model_config = ConfigDict(from_attributes=True)