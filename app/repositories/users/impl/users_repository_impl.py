from sqlalchemy.exc import SQLAlchemyError

from ....models import User
from ....schemas import UserRequestModel, UserResponseModel
from typing import List
from ..users_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        super().__init__()

    def create(self, user: UserRequestModel, hash_password: str) -> UserResponseModel:
        try:
            _user = User(username=user.username, password=hash_password)
            self.db.add(_user)
            self.db.commit()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _user

    def get_all(self, page: int = 1, limit: int = 10) -> List[UserResponseModel]:
        try:
            offset = (page - 1) * limit
            _users = self.db.query(User).offset(offset).limit(limit).all()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return [user for user in _users]

    def get(self, user_id: int) -> UserResponseModel:
        try:
            _user = self.db.query(User).filter(User.id == user_id).first()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _user

    def get_by_credentials(self, username: str, password: str) -> UserResponseModel:
        try:
            _user = self.db.query(User)\
                .filter(User.username == username) \
                .filter(User.password == password) \
                .first()

        except SQLAlchemyError as e:
            self.db.rollback()
            raise

        return _user
