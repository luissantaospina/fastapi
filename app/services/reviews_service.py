from ..repositories.reviews.impl import ReviewRepositoryImpl
from fastapi import Path
from ..models import User
from typing import List

from ..schemas import ReviewRequestPutModel, ReviewResponseModel, ReviewRequestModel


class ReviewService:
    review_repository = ReviewRepositoryImpl()

    @classmethod
    def create_review(cls, review: ReviewRequestModel, user: User) -> ReviewResponseModel:
        review = cls.review_repository.create(review, user)
        return review

    @classmethod
    def get_reviews(cls, page: int = 1, limit: int = 10) -> List[ReviewResponseModel]:
        reviews = cls.review_repository.get_all(page, limit)
        return [review for review in reviews]

    @classmethod
    def get_review(cls, review_id: int) -> ReviewResponseModel:
        review = cls.review_repository.get(review_id)
        return review

    @classmethod
    def update_review(cls, review_request: ReviewRequestPutModel, review_id: int = Path(ge=1))\
            -> ReviewResponseModel:
        review = cls.review_repository.update(review_request, review_id)
        return review

    @classmethod
    def delete_review(cls, review_id: int) -> ReviewResponseModel:
        review = cls.review_repository.delete(review_id)
        return review
