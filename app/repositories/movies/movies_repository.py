from typing import List
from ...database import get_db_session
from abc import ABC, abstractmethod
from ...schemas import MovieRequestModel, MovieResponseModel

db_dependency = next(get_db_session())


class MovieRepository(ABC):
    def __init__(self):
        self.db = db_dependency

    @abstractmethod
    def create(self, movie: MovieRequestModel) -> MovieResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int = 1, limit: int = 10) -> List[MovieResponseModel]:
        pass

    @abstractmethod
    def get(self, movie_id: int) -> MovieResponseModel:
        pass

    @abstractmethod
    def update(self, movie_request: MovieRequestModel, movie_id: int) -> MovieResponseModel:
        pass

    @abstractmethod
    def delete(self, movie_id: int) -> MovieResponseModel:
        pass
