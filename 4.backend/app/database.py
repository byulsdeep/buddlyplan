from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# The connection string for our PostgreSQL database
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# The engine is the core interface to the database.
# The 'connect_args' is only needed for SQLite, not for PostgreSQL.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of SessionLocal will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We will inherit from this class to create each of the ORM models.
Base = declarative_base()

# === ADD THIS FUNCTION ===
def get_db():
    """
    FastAPI dependency to get a database session.
    Ensures the session is always closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()