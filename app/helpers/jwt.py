import jwt
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from ..models.user import User
from os import getenv
from ..repositories.users.impl import UserRepositoryImpl
from dotenv import load_dotenv

load_dotenv()
oauth_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')


def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return encode_token(data)


def decode_token(token: str = Depends(oauth_schema)):
    try:
        return jwt.decode(token, getenv('SECRET_KEY'), algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def encode_token(data: dict):
    try:
        return jwt.encode(data, getenv('SECRET_KEY'), algorithm="HS256")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_user_by_token(token: str = Depends(oauth_schema)) -> User:
    _data = decode_token(token)
    _user = UserRepositoryImpl().get(_data['user_id'])
    return _user
