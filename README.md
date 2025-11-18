# Campaigns FastAPI Backend

Simple assignment-ready backend that exposes campaign data through FastAPI and SQLAlchemy.

## Requirements
- Python 3.11+
- SQLite locally (or any Postgres-compatible DB on Railway)

## Setup
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Environment
Create `.env` with:
```
DATABASE_URL=sqlite:///./db.sqlite  # or postgres://...
ALLOWED_ORIGINS=http://localhost:5173
```

## Database Seeding
- Run `python -m app.seed_db` to programmatically insert 10 rows, **or**
- Execute `sqlite3 db.sqlite < schema_and_seed.sql` (works for Postgres too).

## Railway Deployment
1. Set `DATABASE_URL` and `PORT` variables in Railway.
2. Command: `uvicorn app.main:app --host 0.0.0.0 --port ${PORT}`.
3. Use the included SQL file or `app/seed_db.py` to ensure sample data exists.

## API
- `GET /health` → `{ "status": "ok" }`
- `GET /campaigns?status=Active` → List campaigns (filter optional, case-insensitive).

### Example Requests
```bash
curl -s http://localhost:8000/health
# {"status":"ok"}

curl -s "http://localhost:8000/campaigns?status=active"
# [
#   {"id":1,"name":"Summer Sale","status":"Active","clicks":150,"cost":45.99,"impressions":1200},
#   ...
# ]
```

Each response conforms to `app/schemas.py`, keeping the frontend payload predictable.

