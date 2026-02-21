from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:///fastapi.db"
engine = create_engine(db_url)

# factory that creates sessions to interact with db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model which tracks models
Base = declarative_base()


# used by APIs for creating session for request and closing them after usage
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
