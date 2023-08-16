from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ..reviews_repository import ReviewRepository
from ....models import User, Review, Movie
from typing import List, Type
from ....schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel


class ReviewRepositoryImpl(ReviewRepository):
    @staticmethod
    def validate_review(review_id: int, db: Session) -> Review:
        _review = db.query(Review).filter(Review.id == review_id).first()
        if not _review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

        return _review

    @staticmethod
    def validate_movie(movie_id: int, db: Session) -> None:
        _movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if not _movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')

    def create(self, review: ReviewRequestModel, user: User, db: Session) -> ReviewResponseModel:
        try:
            self.validate_movie(review.movie_id, db)
            _review = Review(
                movie_id=review.movie_id,
                user_id=user.id,
                review=review.review,
                score=review.score
            )
            db.add(_review)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _review

    def get_all(self, page: int, limit: int, db: Session) -> List[Type[Review]]:
        try:
            _offset = (page - 1) * limit
            _reviews = db.query(Review).offset(_offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _reviews

    def get(self, review_id: int, db: Session) -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id, db)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _review

    def update(self, review_request: ReviewRequestPutModel, review_id: int, db: Session) \
            -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id, db)
            _review.review = review_request.review
            _review.score = review_request.score
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _review

    def delete(self, review_id: int, db: Session) -> ReviewResponseModel:
        try:
            _review = self.validate_review(review_id, db)
            db.delete(_review)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _review
