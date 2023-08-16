from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserRequestModel, UserResponseModel
from fastapi import APIRouter, Path, Depends
from ..services import UserService
from typing import List


router = APIRouter(
    prefix='/users',
    tags=["users"]
)


@router.post("", response_model=UserResponseModel)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db)) -> UserResponseModel:
    user_created = UserService.create_user(user, db)
    return user_created


@router.get("", response_model=List[UserResponseModel])
async def get_users(page: int = 1, limit: int = 10, db: Session = Depends(get_db)) \
        -> List[UserResponseModel]:
    users = UserService.get_users(page, limit, db)
    return users


@router.get("/{user_id}", response_model=UserResponseModel)
def get_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)) -> UserResponseModel:
    user = UserService.get_user(user_id, db)
    return user
