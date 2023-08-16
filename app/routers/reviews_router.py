from typing import List, Annotated
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import ReviewRequestModel, \
    ReviewResponseModel, \
    ReviewRequestPutModel
from fastapi import APIRouter, Depends, Path
from ..helpers import oauth2_scheme
from ..models import User
from ..helpers import get_user_by_token
from ..services import ReviewService

router = APIRouter(
    prefix='/reviews',
    tags=["reviews"],
    dependencies=[Depends(oauth2_scheme)]
)


@router.post("", response_model=ReviewResponseModel)
async def create_review(review: ReviewRequestModel, user: Annotated[User, Depends(get_user_by_token)],
                        db: Session = Depends(get_db)) -> ReviewResponseModel:
    review_created = ReviewService.create_review(review, user, db)
    return review_created


@router.get("", response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10, db: Session = Depends(get_db))\
        -> List[ReviewResponseModel]:
    reviews = ReviewService.get_reviews(page, limit, db)
    return reviews


@router.get("/{review_id}", response_model=ReviewResponseModel)
def get_review(review_id: int = Path(ge=1), db: Session = Depends(get_db)) -> ReviewResponseModel:
    review = ReviewService.get_review(review_id, db)
    return review


@router.put("/{review_id}", response_model=ReviewResponseModel)
async def update_review(review_request: ReviewRequestPutModel, review_id: int = Path(ge=1),
                        db: Session = Depends(get_db)) -> ReviewResponseModel:
    review_updated = ReviewService.update_review(review_request, review_id, db)
    return review_updated


@router.delete("/{review_id}", response_model=ReviewResponseModel)
def delete_review(review_id: int = Path(ge=1), db: Session = Depends(get_db)) -> ReviewResponseModel:
    review_deleted = ReviewService.delete_review(review_id, db)
    return review_deleted
