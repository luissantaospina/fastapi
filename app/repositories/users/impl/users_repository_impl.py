from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ....models import User
from ....schemas import UserRequestModel, UserResponseModel
from typing import List
from ..users_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        super().__init__()

    def validate_user(self, user_id: int) -> User:
        _user = self.db.query(User).filter(User.id == user_id).first()
        if not _user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return _user

    def validate_username(self, username: str) -> None:
        _user = self.db.query(User).filter(User.username == username).first()
        if _user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username exist')

    def create(self, user: UserRequestModel, hash_password: str) -> UserResponseModel:
        try:
            self.validate_username(user.username)
            _user = User(username=user.username, password=hash_password)
            self.db.add(_user)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        return _user

    def get_all(self, page: int = 1, limit: int = 10) -> List[UserResponseModel]:
        try:
            offset = (page - 1) * limit
            _users = self.db.query(User).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return [user for user in _users]

    def get(self, user_id: int) -> UserResponseModel:
        try:
            _user = self.validate_user(user_id)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return _user

    def get_by_credentials(self, username: str, password: str) -> UserResponseModel:
        try:
            _user = self.db.query(User)\
                .filter(User.username == username) \
                .filter(User.password == password) \
                .first()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=str(e))

        return _user
