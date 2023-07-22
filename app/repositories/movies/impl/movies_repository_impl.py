from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..movies_repository import MovieRepository
from ....models import Movie
from ....schemas import MovieRequestModel, MovieResponseModel


class MovieRepositoryImpl(MovieRepository):
    def __init__(self):
        super().__init__()

    def validate_movie(self, movie_id: int) -> Movie:
        _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        if not _movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')

        return _movie

    def create(self, movie: MovieRequestModel) -> MovieResponseModel:
        try:
            _movie = Movie(title=movie.title)
            self.db.add(_movie)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _movie

    def get_all(self, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        try:
            offset = (page - 1) * limit
            _movies = self.db.query(Movie).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return [movie for movie in _movies]

    def get(self, movie_id: int) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return _movie

    def update(self, movie_request: MovieRequestModel, movie_id: int) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id)
            _movie.title = movie_request.title
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _movie

    def delete(self, movie_id: int) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id)
            self.db.delete(_movie)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _movie
