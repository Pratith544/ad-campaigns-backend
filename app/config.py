import os
from dotenv import load_dotenv

load_dotenv()

# Required for CORS
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]

# Required for the DB connection
DATABASE_URL = os.getenv("DATABASE_URL")
