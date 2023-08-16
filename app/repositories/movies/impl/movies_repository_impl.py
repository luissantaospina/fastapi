from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ..movies_repository import MovieRepository
from ....models import Movie
from ....schemas import MovieRequestModel, MovieResponseModel


class MovieRepositoryImpl(MovieRepository):
    @staticmethod
    def validate_movie(movie_id: int, db: Session) -> Movie:
        _movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if not _movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')

        return _movie

    def create(self, movie: MovieRequestModel, db: Session) -> MovieResponseModel:
        try:
            _movie = Movie(title=movie.title)
            db.add(_movie)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _movie

    def get_all(self, page: int, limit: int, db: Session) -> List[MovieResponseModel]:
        try:
            _offset = (page - 1) * limit
            _movies = db.query(Movie).offset(_offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _movies

    def get(self, movie_id: int, db: Session) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id, db)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _movie

    def update(self, movie_request: MovieRequestModel, movie_id: int, db: Session) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id, db)
            _movie.title = movie_request.title
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _movie

    def delete(self, movie_id: int, db: Session) -> MovieResponseModel:
        try:
            _movie = self.validate_movie(movie_id, db)
            db.delete(_movie)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _movie
