from fastapi import Depends, HTTPException, status
from ..models import User
from fastapi.security import OAuth2PasswordRequestForm, HTTPBasicCredentials
from ..helpers import create_access_token, get_current_user, encode_password
from fastapi import APIRouter

from ..repositories.users.impl import UserRepositoryImpl
from ..schemas import UserResponseModel
from ..services import AuthService

router = APIRouter(prefix='/auth', tags=["auth"])


@router.post("/login", response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials):
    _password = encode_password(credentials.password)
    _user = UserRepositoryImpl().get_by_credentials(credentials.username, _password)

    if not _user:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return _user


@router.post('')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    _user = AuthService.authenticate(data.username, data.password)
    if not _user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
    return {'access_token': create_access_token(_user), 'token_type': 'Bearer'}


@router.get('', response_model=UserResponseModel)
async def get_user_from_token(user: User = Depends(get_current_user)):
    return user
