from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv
from ..models import User
from ..models import Review
from ..models import Movie

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


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models = [
    User,
    Movie,
    Review
]


def create_all_tables():
    for model in models:
        model.metadata.create_all(bind=engine)
