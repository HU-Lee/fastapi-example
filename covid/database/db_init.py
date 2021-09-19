import os
from dotenv.main import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session

load_dotenv(verbose=True)

POSTGRES_URL = os.getenv("POSTGRES_URL")

engine = create_engine(POSTGRES_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db() -> Session:
    try:
        db:Session = SessionLocal()
        print("DB connected...")
        return db
    finally:
        db.close()

Base = declarative_base()
Base.query = SessionLocal.query_property()