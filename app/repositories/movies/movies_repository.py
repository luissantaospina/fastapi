from typing import List
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from ...schemas import MovieRequestModel, MovieResponseModel


class MovieRepository(ABC):
    @abstractmethod
    def create(self, movie: MovieRequestModel, db: Session) -> MovieResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[MovieResponseModel]:
        pass

    @abstractmethod
    def get(self, movie_id: int, db: Session) -> MovieResponseModel:
        pass

    @abstractmethod
    def update(self, movie_request: MovieRequestModel, movie_id: int, db: Session) -> MovieResponseModel:
        pass

    @abstractmethod
    def delete(self, movie_id: int, db: Session) -> MovieResponseModel:
        pass
