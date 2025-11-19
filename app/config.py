import os
from dotenv import load_dotenv

load_dotenv()


ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]


DATABASE_URL = os.getenv("DATABASE_URL")
