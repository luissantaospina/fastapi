from fastapi import HTTPException, status
from ..helpers import encode_password
from ..repositories.users.impl import UserRepositoryImpl
from ..schemas import UserResponseModel


class AuthService:
    @staticmethod
    def authenticate(username: str, password: str) -> UserResponseModel:
        _password = encode_password(password)
        _user = UserRepositoryImpl().get_by_credentials(username, _password)

        if not _user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')

        if not _user.is_activate:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User is not active')

        return _user
