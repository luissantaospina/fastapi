from typing import List
from fastapi import Path
from ..schemas import MovieRequestModel, MovieResponseModel
from ..repositories.movies.impl import MovieRepositoryImpl


class MovieService:
    user_repository = MovieRepositoryImpl()

    @classmethod
    def create_movie(cls, movie: MovieRequestModel) -> MovieResponseModel:
        movie = cls.user_repository.create(movie)
        return movie

    @classmethod
    def get_movies(cls, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        movies = cls.user_repository.get_all(page, limit)
        return [movie for movie in movies]

    @classmethod
    def get_movie(cls, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        movie = cls.user_repository.get(movie_id)
        return movie

    @classmethod
    def update_movie(cls, movie_request: MovieRequestModel, movie_id: int = Path(ge=1)) \
            -> MovieResponseModel:
        movie = cls.user_repository.update(movie_request, movie_id)
        return movie

    @classmethod
    def delete_movie(cls, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        movie = cls.user_repository.delete(movie_id)
        return movie
