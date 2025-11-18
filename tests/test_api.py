import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app, _normalize_status
from app.database import Base, get_db
from app import models


# Create an in-memory SQLite database for tests
engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)


def seed_data():
    db = TestingSessionLocal()
    try:
        db.add_all(
            [
                models.Campaign(
                    name="Demo Active",
                    status="Active",
                    clicks=10,
                    cost=1.5,
                    impressions=100,
                ),
                models.Campaign(
                    name="Demo Paused",
                    status="Paused",
                    clicks=5,
                    cost=0.5,
                    impressions=50,
                ),
            ]
        )
        db.commit()
    finally:
        db.close()


seed_data()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_campaigns_returns_data():
    response = client.get("/campaigns")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert any(c["status"] == "Active" for c in payload)


@pytest.mark.parametrize("status_input", ["active", "ACTIVE", "Paused"])
def test_campaigns_filter_case_insensitive(status_input):
    response = client.get("/campaigns", params={"status": status_input})
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) >= 1
    assert all(c["status"].lower() == status_input.lower() for c in payload)


