from ..schemas import UserRequestModel, UserResponseModel
from ..repositories.users.impl import UserRepositoryImpl
from typing import List
from ..helpers import encode_password


class UserService:
    user_repository = UserRepositoryImpl()

    @classmethod
    def create_user(cls, user: UserRequestModel) -> UserResponseModel:
        hash_password = encode_password(user.password)
        user = cls.user_repository.create(user, hash_password)
        return user

    @classmethod
    def get_users(cls, page: int = 1, limit: int = 10) -> List[UserResponseModel]:
        users = cls.user_repository.get_all(page, limit)
        return [user for user in users]

    @classmethod
    def get_user(cls, user_id: int) -> UserResponseModel:
        user = cls.user_repository.get(user_id)
        return user
