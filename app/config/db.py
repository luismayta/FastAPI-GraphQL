from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

SQLALCHEMY_DATABASE = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_instance():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
