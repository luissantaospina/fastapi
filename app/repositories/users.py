from ..models import User
from ..schemas import UserRequestModel, UserResponseModel


class UserRepository:
    @classmethod
    def create(cls, user: UserRequestModel, hash_password: str) -> UserResponseModel:
        user = User.create(
            username=user.username,
            password=hash_password
        )
        return user
