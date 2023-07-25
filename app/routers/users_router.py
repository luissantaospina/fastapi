from ..schemas import UserRequestModel, UserResponseModel
from fastapi import APIRouter, Path
from ..services import UserService
from typing import List


router = APIRouter(
    prefix='/users',
    tags=["users"]
)


@router.post("", response_model=UserResponseModel)
async def create_user(user: UserRequestModel) -> UserResponseModel:
    user_created = UserService.create_user(user)
    return user_created


@router.get("", response_model=List[UserResponseModel])
async def get_users(page: int = 1, limit: int = 10) -> List[UserResponseModel]:
    users = UserService.get_users(page, limit)
    return [user for user in users]


@router.get("/{user_id}", response_model=UserResponseModel)
def get_user(user_id: int = Path(ge=1)) -> UserResponseModel:
    user = UserService.get_user(user_id)
    return user
