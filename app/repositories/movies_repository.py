from typing import List
from fastapi import Path
from ..models import Movie
from ..schemas import MovieRequestModel, MovieResponseModel


class MovieRepository:

    @classmethod
    def create(cls, movie: MovieRequestModel) -> MovieResponseModel:
        movie = Movie.create(title=movie.title)
        return movie

    @classmethod
    def get_all(cls, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        movies = Movie.select().paginate(page, limit)
        return [movie for movie in movies]

    @classmethod
    def get(cls, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        movie = Movie.select().where(Movie.id == movie_id).first()
        return movie

    @classmethod
    def update(cls, movie_request: MovieRequestModel, movie_id: int = Path(ge=1)) \
            -> MovieResponseModel:
        movie = Movie.select().where(Movie.id == movie_id).first()
        movie.title = movie_request.title
        movie.save()
        return movie

    @classmethod
    def delete(cls, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        movie = Movie.select().where(Movie.id == movie_id).first()
        movie.delete_instance()
        return movie
