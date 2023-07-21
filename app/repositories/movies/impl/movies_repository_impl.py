from typing import List
from fastapi import Path
from ..movies_repository import MovieRepository
from ....models import Movie
from ....schemas import MovieRequestModel, MovieResponseModel


class MovieRepositoryImpl(MovieRepository):
    def __init__(self):
        super().__init__()

    def create(self, movie: MovieRequestModel) -> MovieResponseModel:
        _movie = Movie(title=movie.title)
        self.db.add(_movie)
        self.db.commit()
        return _movie

    def get_all(self, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        offset = (page - 1) * limit
        _movies = self.db.query(Movie).offset(offset).limit(limit).all()
        return [movie for movie in _movies]

    def get(self, movie_id: int = Path(ge=1)) -> MovieResponseModel:
        _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        return _movie

    def update(self, movie_request: MovieRequestModel, movie_id: int) -> MovieResponseModel:
        _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        _movie.title = movie_request.title
        self.db.commit()
        return _movie

    def delete(self, movie_id: int) -> MovieResponseModel:
        _movie = self.db.query(Movie).filter(Movie.id == movie_id).first()
        self.db.delete(_movie)
        self.db.commit()
        return _movie
