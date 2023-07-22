from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..reviews_repository import ReviewRepository
from ....models import User, Review
from typing import List
from ....schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel


class ReviewRepositoryImpl(ReviewRepository):
    def __init__(self):
        super().__init__()

    def validate_review(self, review_id: int) -> Review:
        _review = self.db.query(Review).filter(Review.id == review_id).first()
        if not _review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

        return _review

    def create(self, review: ReviewRequestModel, user: User) -> ReviewResponseModel:
        try:
            _review = Review(
                movie_id=review.movie_id,
                user_id=user.id,
                review=review.review,
                score=review.score
            )
            self.db.add(_review)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _review

    def get_all(self, page: int = 1, limit: int = 10) -> List[ReviewResponseModel]:
        try:
            offset = (page - 1) * limit
            reviews = self.db.query(Review).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return [review for review in reviews]

    def get(self, review_id: int) -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return _review

    def update(self, review_request: ReviewRequestPutModel, review_id: int) \
            -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id)
            _review.review = review_request.review
            _review.score = review_request.score
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _review

    def delete(self, review_id: int) -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id)
            self.db.delete(_review)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _review
