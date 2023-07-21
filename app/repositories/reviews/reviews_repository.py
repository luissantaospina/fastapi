from ...models import User
from ...schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel
from typing import List
from ...database import get_db_session
from abc import ABC, abstractmethod

db_dependency = next(get_db_session())


class ReviewRepository(ABC):
    def __init__(self):
        self.db = db_dependency

    @abstractmethod
    def create(self, review: ReviewRequestModel, user: User) -> ReviewResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int = 1, limit: int = 10) -> List[ReviewResponseModel]:
        pass

    @abstractmethod
    def get(self, review_id: int) -> ReviewResponseModel:
        pass

    @abstractmethod
    def update(self, review_request: ReviewRequestPutModel, review_id: int) -> ReviewResponseModel:
        pass

    @abstractmethod
    def delete(self, review_id: int) -> ReviewResponseModel:
        pass
