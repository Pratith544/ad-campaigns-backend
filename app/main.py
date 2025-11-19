from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
import logging

from .database import engine, Base, get_db
from . import models, schemas, crud
from .config import ALLOWED_ORIGINS

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Campaigns API", version="1.0")


logger = logging.getLogger("uvicorn.error")


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS or ["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    """Ensure the schema exists when the service boots."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database schema checked/created.")


@app.get("/health", tags=["health"])
def healthcheck():
    return {"status": "ok"}


def _normalize_status(status: Optional[str]) -> Optional[str]:
    if status is None:
        return None
    normalized = status.strip().lower()
    allowed = {"active", "paused"}
    if normalized not in allowed:
        raise HTTPException(status_code=400, detail="status must be 'Active' or 'Paused'")
    return normalized.capitalize()


@app.get("/campaigns", response_model=List[schemas.Campaign], tags=["campaigns"])
def read_campaigns(
    status: Optional[str] = Query(None, description="Filter by status: Active or Paused"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    normalized_status = _normalize_status(status)
    campaigns = crud.get_campaigns(db=db, status=normalized_status, limit=limit, offset=offset)
    return campaigns