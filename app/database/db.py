from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = 'mysql+mysqlconnector://{user}:{pss}@{host}:{port}/{db}'.format(
    user=getenv("PGSQL_USER"),
    pss=getenv("PGSQL_PASSWORD"),
    host=getenv("PGSQL_HOST"),
    port=getenv("PGSQL_PORT"),
    db=getenv("PGSQL_DATABASE")
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
