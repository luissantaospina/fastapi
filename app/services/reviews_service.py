from sqlalchemy.orm import Session
from ..repositories.reviews.impl import ReviewRepositoryImpl
from ..models import User
from typing import List

from ..schemas import ReviewRequestPutModel, ReviewResponseModel, ReviewRequestModel


class ReviewService:
    review_repository = ReviewRepositoryImpl()

    @classmethod
    def create_review(cls, review: ReviewRequestModel, user: User, db: Session) -> ReviewResponseModel:
        review = cls.review_repository.create(review, user, db)
        return review

    @classmethod
    def get_reviews(cls, page: int, limit: int, db: Session) -> List[ReviewResponseModel]:
        reviews = cls.review_repository.get_all(page, limit, db)
        return reviews

    @classmethod
    def get_review(cls, review_id: int, db: Session) -> ReviewResponseModel:
        review = cls.review_repository.get(review_id, db)
        return review

    @classmethod
    def update_review(cls, review_request: ReviewRequestPutModel, review_id: int, db: Session)\
            -> ReviewResponseModel:
        review = cls.review_repository.update(review_request, review_id, db)
        return review

    @classmethod
    def delete_review(cls, review_id: int, db: Session) -> ReviewResponseModel:
        review = cls.review_repository.delete(review_id, db)
        return review
