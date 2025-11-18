from .database import SessionLocal, engine, Base
from . import crud
from . import models

def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Check if any campaigns exist
        if db.query(models.Campaign).count() > 0:
            print("DB already seeded.")
            return

        samples = [
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

        for name, status, clicks, cost, impressions in samples:
            crud.create_campaign(db=db, name=name, status=status, clicks=clicks, cost=cost, impressions=impressions)

        print("Seeded DB with sample campaigns.")
    finally:
        db.close()

if __name__ == "__main__":
    run()