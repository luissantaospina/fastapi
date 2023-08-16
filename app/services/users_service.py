from sqlalchemy.orm import Session
from ..schemas import UserRequestModel, UserResponseModel
from ..repositories.users.impl import UserRepositoryImpl
from typing import List
from ..helpers import encode_password


class UserService:
    user_repository = UserRepositoryImpl()

    @classmethod
    def create_user(cls, user: UserRequestModel, db: Session) -> UserResponseModel:
        hash_password = encode_password(user.password)
        user = cls.user_repository.create(user, hash_password, db)
        return user

    @classmethod
    def get_users(cls, page: int, limit: int, db: Session) -> List[UserResponseModel]:
        users = cls.user_repository.get_all(page, limit, db)
        return users

    @classmethod
    def get_user(cls, user_id: int, db: Session) -> UserResponseModel:
        user = cls.user_repository.get(user_id, db)
        return user
