from ..schemas import UserReviewRequestModel, UserReviewRequestPutModel, UserReviewResponseModel
from fastapi import Path
from ..models import User
from typing import List
from ..repositories import UserReviewRepository


class UserReviewService:

    @classmethod
    def create_review(cls, review: UserReviewRequestModel, user: User) -> UserReviewResponseModel:
        review = UserReviewRepository.create(review, user)
        return review

    @classmethod
    def get_reviews(cls, page: int = 1, limit: int = 10) -> List[UserReviewResponseModel]:
        reviews = UserReviewRepository.get_all(page, limit)
        return [review for review in reviews]

    @classmethod
    def get_review(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = UserReviewRepository.get(review_id)
        return review

    @classmethod
    def update_review(cls, review_request: UserReviewRequestPutModel, review_id: int = Path(ge=1))\
            -> UserReviewResponseModel:
        review = UserReviewRepository.update(review_request, review_id)
        return review

    @classmethod
    def delete_review(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = UserReviewRepository.delete(review_id)
        return review
