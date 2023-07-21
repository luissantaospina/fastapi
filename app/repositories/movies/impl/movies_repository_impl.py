from typing import List
from fastapi import Path
from sqlalchemy.exc import SQLAlchemyError
from ..movies_repository import MovieRepository
from ....models import Movie
from ....schemas import MovieRequestModel, MovieResponseModel


class MovieRepositoryImpl(MovieRepository):
    def __init__(self):
        super().__init__()

    def create(self, movie: MovieRequestModel) -> MovieResponseModel:
        try:
            _movie = Movie(title=movie.title)
            self.db.add(_movie)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _movie

    def get_all(self, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        try:
            offset = (page - 1) * limit
            _movies = self.db.query(Movie).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return [movie for movie in _movies]

    def get(self, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        try:
            _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _movie

    def update(self, movie_request: MovieRequestModel, movie_id: int) -> MovieResponseModel:
        try:
            _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
            _movie.title = movie_request.title
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _movie

    def delete(self, movie_id: int) -> MovieResponseModel:
        try:
            _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
            self.db.delete(_movie)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _movie
