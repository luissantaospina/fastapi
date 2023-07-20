from fastapi import Depends, HTTPException, status
from ..models import User
from fastapi.security import OAuth2PasswordRequestForm
from ..helpers import create_access_token, get_current_user
from fastapi import APIRouter
from ..schemas import UserResponseModel

router = APIRouter(prefix='/auth', tags=["auth"])


@router.post('')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
    return {'access_token': create_access_token(user), 'token_type': 'Bearer'}


@router.get('', response_model=UserResponseModel)
async def get_user_from_token(user: User = Depends(get_current_user)):
    return user
