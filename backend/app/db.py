import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://app:app_password@localhost:5432/ai_companion"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def test_db_connection() -> bool:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True
