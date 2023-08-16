from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..repositories.users.impl import UserRepositoryImpl
from ..schemas import UserResponseModel
import bcrypt


class AuthService:
    def authenticate(self, username: str, password: str, db: Session) -> UserResponseModel:
        _user = UserRepositoryImpl().get_by_username(username, db)

        if not _user or not _user.is_activate or not self.verify_password(password, _user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')

        return _user

    @staticmethod
    def verify_password(input_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))
