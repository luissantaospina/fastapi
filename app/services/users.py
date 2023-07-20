from ..models import User
from ..schemas import UserRequestModel, UserResponseModel
from ..repositories import UserRepository


class UserService:
    @classmethod
    def create_user(cls, user: UserRequestModel) -> UserResponseModel:
        hash_password = User.create_password(user.password)
        user = UserRepository.create(user, hash_password)
        return user
