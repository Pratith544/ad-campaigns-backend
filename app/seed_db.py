import argparse
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud
from . import models

IMAGE_URLS = [
    "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1492725764893-90b379c2b6e7?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1495020689067-958852a7765e?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1200&q=80",
]

CAMPAIGN_SAMPLES = [
    ("Summer Sale", "Active", 150, 45.99, 1200),
    ("Black Friday", "Paused", 320, 89.50, 2500),
    ("New Year Promo", "Active", 210, 65.0, 1800),
    ("Winter Clearance", "Paused", 40, 10.0, 400),
    ("Spring Blast", "Active", 500, 120.0, 5200),
    ("Flash Deal", "Active", 80, 19.99, 800),
    ("Referral Drive", "Paused", 30, 5.0, 300),
    ("Holiday Push", "Active", 240, 70.0, 2200),
    ("Test Campaign 1", "Paused", 0, 0.0, 0),
    ("Test Campaign 2", "Active", 10, 2.5, 100),
]

def _validate_seed_lists() -> None:
    if len(CAMPAIGN_SAMPLES) != len(IMAGE_URLS):
        raise ValueError("CAMPAIGN_SAMPLES and IMAGE_URLS must be the same length.")


def _backfill_image_urls(db: Session) -> None:
    """Ensure existing campaigns have the expected image_url ordering."""
    campaigns = db.query(models.Campaign).order_by(models.Campaign.id).all()
    updated = False
    for campaign, image_url in zip(campaigns, IMAGE_URLS):
        if campaign.image_url != image_url:
            campaign.image_url = image_url
            updated = True
    if updated:
        db.commit()
        print("Backfilled campaign image URLs.")


def _clear_campaigns(db: Session) -> None:
    deleted = db.query(models.Campaign).delete()
    db.commit()
    print(f"Cleared {deleted} existing campaign(s).")


def run(force_reset: bool = False):
    Base.metadata.create_all(bind=engine)
    _validate_seed_lists()

    db = SessionLocal()
    try:
        if force_reset:
            _clear_campaigns(db)

        existing = db.query(models.Campaign).count()
        if existing > 0:
            _backfill_image_urls(db)
            print("DB already seeded; ensured image URLs are correct.")
            return

        for (name, status, clicks, cost, impressions), image_url in zip(CAMPAIGN_SAMPLES, IMAGE_URLS):
            crud.create_campaign(
                db=db,
                name=name,
                status=status,
                clicks=clicks,
                cost=cost,
                impressions=impressions,
                image_url=image_url,
            )

        print("Seeded DB with sample campaigns.")
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser(description="Seed campaigns with image URLs.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing campaigns before seeding.",
    )
    args = parser.parse_args()
    run(force_reset=args.reset)


if __name__ == "__main__":
    main()