from sqlalchemy.orm import Session
from ..database import get_db
from ..helpers import create_access_token
from fastapi import APIRouter
from ..schemas.auth_schema import AuthResponseModel
from ..services import AuthService
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix='/auth', tags=["auth"])


@router.post('/login', response_model=AuthResponseModel)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    _user = AuthService().authenticate(form_data.username, form_data.password, db)

    return {
        'access_token': create_access_token(_user),
        'token_type': 'Bearer',
        'user': _user
    }
