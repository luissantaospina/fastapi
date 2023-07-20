import functools
from typing import List
from ..schemas import UserReviewRequestModel, \
    UserReviewResponseModel, \
    UserReviewRequestPutModel
from fastapi import APIRouter, HTTPException, status, Depends, Path
from ..helpers import oauth_schema
from ..models import User
from ..helpers import get_current_user
from ..services import UserReviewService
from ..repositories import UserReviewRepository

router = APIRouter(
    prefix='/reviews',
    tags=["reviews"],
    dependencies=[Depends(oauth_schema)]
)


def validate_review(function):
    @functools.wraps(function)
    def wrapper(review_id: int):
        review = UserReviewRepository.get(review_id)
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

        return function(review_id)

    return wrapper


@router.post("", response_model=UserReviewResponseModel)
async def create_review(review: UserReviewRequestModel, user: User = Depends(get_current_user))\
        -> UserReviewResponseModel:
    review_created = UserReviewService.create_review(review, user)
    return review_created


@router.get("", response_model=List[UserReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10)\
        -> List[UserReviewResponseModel]:
    reviews = UserReviewService.get_reviews(page, limit)
    return [review for review in reviews]


@router.get("/{review_id}", response_model=UserReviewResponseModel)
@validate_review
def get_review(review_id: int = Path(ge=1)) -> UserReviewResponseModel:
    review = UserReviewService.get_review(review_id)
    return review


# TODO: Validate review
@router.put("/{review_id}", response_model=UserReviewResponseModel)
async def update_review(review_request: UserReviewRequestPutModel, review_id: int = Path(ge=1))\
        -> UserReviewResponseModel:
    review_updated = UserReviewService.update_review(review_request, review_id)
    return review_updated


# with Path validate the route params
@router.delete("/{review_id}", response_model=UserReviewResponseModel)
@validate_review
def delete_review(review_id: int = Path(ge=1)) -> UserReviewResponseModel:
    review_deleted = UserReviewService.delete_review(review_id)
    return review_deleted
