from typing import List
from sqlalchemy.orm import Session
from ..schemas import MovieRequestModel, MovieResponseModel
from ..repositories.movies.impl import MovieRepositoryImpl


class MovieService:
    user_repository = MovieRepositoryImpl()

    @classmethod
    def create_movie(cls, movie: MovieRequestModel, db: Session) -> MovieResponseModel:
        movie = cls.user_repository.create(movie, db)
        return movie

    @classmethod
    def get_movies(cls, page: int, limit: int, db: Session) -> List[MovieResponseModel]:
        movies = cls.user_repository.get_all(page, limit, db)
        return movies

    @classmethod
    def get_movie(cls, movie_id: int, db: Session) -> MovieResponseModel:
        movie = cls.user_repository.get(movie_id, db)
        return movie

    @classmethod
    def update_movie(cls, movie_request: MovieRequestModel, movie_id: int, db: Session) \
            -> MovieResponseModel:
        movie = cls.user_repository.update(movie_request, movie_id, db)
        return movie

    @classmethod
    def delete_movie(cls, movie_id: int, db: Session) -> MovieResponseModel:
        movie = cls.user_repository.delete(movie_id, db)
        return movie
