from ..models import Review
from ..schemas import UserReviewRequestModel, UserReviewRequestPutModel, UserReviewResponseModel
from fastapi import Path
from ..models import User
from typing import List


class UserReviewRepository:

    @classmethod
    def create(cls, review: UserReviewRequestModel, user: User) -> UserReviewResponseModel:
        review = Review.create(
            movie_id=review.movie_id,
            user_id=user.id,
            review=review.review,
            score=review.score
        )
        return review

    @classmethod
    def get_all(cls, page: int = 1, limit: int = 10) -> List[UserReviewResponseModel]:
        reviews = Review.select().paginate(page, limit)
        return [review for review in reviews]

    @classmethod
    def get(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = Review.select().where(Review.id == review_id).first()
        return review

    @classmethod
    def update(cls, review_request: UserReviewRequestPutModel, review_id: int = Path(ge=1))\
            -> UserReviewResponseModel:
        review = Review.select().where(Review.id == review_id).first()
        review.review = review_request.review
        review.score = review_request.score
        review.save()
        return review

    @classmethod
    def delete(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = Review.select().where(Review.id == review_id).first()
        review.delete_instance()
        return review
