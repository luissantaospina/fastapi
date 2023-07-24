from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..helpers import create_access_token
from fastapi import APIRouter
from ..schemas.auth_schema import AuthResponseModel
from ..services import AuthService

router = APIRouter(prefix='/auth', tags=["auth"])


@router.post('/login', response_model=AuthResponseModel)
async def login(data: OAuth2PasswordRequestForm = Depends()):
    _user = AuthService().authenticate(data.username, data.password)

    return {
        'access_token': create_access_token(_user),
        'token_type': 'Bearer',
        'user': _user
    }
