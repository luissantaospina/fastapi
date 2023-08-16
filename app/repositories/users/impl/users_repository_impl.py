from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ....models import User
from ....schemas import UserRequestModel, UserResponseModel
from typing import List, Type
from ..users_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    @staticmethod
    def validate_user(user_id: int, db: Session) -> User:
        _user = db.query(User).filter(User.id == user_id).first()
        if not _user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        return _user

    @staticmethod
    def validate_username(username: str, db: Session) -> None:
        _user = db.query(User).filter(User.username == username).first()
        if _user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username exist')

    def create(self, user: UserRequestModel, hash_password: str, db: Session) -> UserResponseModel:
        try:
            self.validate_username(user.username, db)
            _user = User(username=user.username, password=hash_password)
            db.add(_user)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _user

    def get_all(self, page: int, limit: int, db: Session) -> List[Type[User]]:
        try:
            offset = (page - 1) * limit
            _users = db.query(User).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _users

    def get(self, user_id: int, db: Session) -> UserResponseModel:
        try:
            _user = self.validate_user(user_id, db)

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _user

    def get_by_username(self, username: str, db: Session) -> User:
        try:
            _user = db.query(User).filter(User.username == username).first()

        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return _user
