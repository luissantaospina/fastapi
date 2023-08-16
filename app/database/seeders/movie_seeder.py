from app.database import get_db
from app.models import Movie

db = next(get_db())


def seed_movies():
    movies = [
        Movie(title="Alice"),
        Movie(title="Bob")
    ]

    db.add_all(movies)
    db.commit()
