from app.database import get_db_session
from app.models import Movie

db = next(get_db_session())


def seed_movies():
    movies = [
        Movie(title="Alice"),
        Movie(title="Bob")
    ]

    db.add_all(movies)
    db.commit()
