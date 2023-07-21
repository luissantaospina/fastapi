import functools
from typing import List
from ..repositories.reviews.impl import ReviewRepositoryImpl
from ..schemas import ReviewRequestModel, \
    ReviewResponseModel, \
    ReviewRequestPutModel
from fastapi import APIRouter, HTTPException, status, Depends, Path
from ..helpers import oauth_schema
from ..models import User
from ..helpers import get_current_user
from ..services import ReviewService

router = APIRouter(
    prefix='/reviews',
    tags=["reviews"],
    dependencies=[Depends(oauth_schema)]
)


def validate_review(function):
    @functools.wraps(function)
    def wrapper(review_id: int):
        review = ReviewRepositoryImpl().get(review_id)
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

        return function(review_id)

    return wrapper


@router.post("", response_model=ReviewResponseModel)
async def create_review(review: ReviewRequestModel, user: User = Depends(get_current_user))\
        -> ReviewResponseModel:
    review_created = ReviewService.create_review(review, user)
    return review_created


@router.get("", response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10)\
        -> List[ReviewResponseModel]:
    reviews = ReviewService.get_reviews(page, limit)
    return [review for review in reviews]


@router.get("/{review_id}", response_model=ReviewResponseModel)
@validate_review
def get_review(review_id: int = Path(ge=1)) -> ReviewResponseModel:
    review = ReviewService.get_review(review_id)
    return review


# TODO: Validate review
@router.put("/{review_id}", response_model=ReviewResponseModel)
async def update_review(review_request: ReviewRequestPutModel, review_id: int = Path(ge=1))\
        -> ReviewResponseModel:
    review_updated = ReviewService.update_review(review_request, review_id)
    return review_updated


@router.delete("/{review_id}", response_model=ReviewResponseModel)
@validate_review
def delete_review(review_id: int = Path(ge=1)) -> ReviewResponseModel:
    review_deleted = ReviewService.delete_review(review_id)
    return review_deleted
