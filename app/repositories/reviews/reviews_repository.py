from sqlalchemy.orm import Session
from ...models import User
from ...schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel
from typing import List
from abc import ABC, abstractmethod


class ReviewRepository(ABC):
    @abstractmethod
    def create(self, review: ReviewRequestModel, user: User, db: Session) -> ReviewResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[ReviewResponseModel]:
        pass

    @abstractmethod
    def get(self, review_id: int, db: Session) -> ReviewResponseModel:
        pass

    @abstractmethod
    def update(self, review_request: ReviewRequestPutModel, review_id: int, db: Session) -> ReviewResponseModel:
        pass

    @abstractmethod
    def delete(self, review_id: int, db: Session) -> ReviewResponseModel:
        pass
