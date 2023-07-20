from ..models import User
from ..schemas import UserRequestModel, UserResponseModel
from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasicCredentials
from ..services import UserService
from ..database import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users',
    tags=["users"]
)


@router.post("", response_model=UserResponseModel)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db_session)) -> UserResponseModel:
    user_created = UserService.create_user(user, db)
    return user_created


@router.post("/login", response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials):
    password = User.create_password(credentials.password)
    user = User.select()\
        .where(User.username == credentials.username) \
        .where(User.password == password) \
        .first()

    if not user:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return user
