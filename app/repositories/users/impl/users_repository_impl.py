from ....models import User
from ....schemas import UserRequestModel, UserResponseModel
from typing import List
from ..users_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        super().__init__()

    def create(self, user: UserRequestModel, hash_password: str) -> UserResponseModel:
        _user = User(username=user.username, password=hash_password)
        self.db.add(_user)
        self.db.commit()
        return _user

    def get_all(self, page: int = 1, limit: int = 10) -> List[UserResponseModel]:
        offset = (page - 1) * limit
        _users = self.db.query(User).offset(offset).limit(limit).all()
        return [user for user in _users]

    def get(self, user_id: int) -> UserResponseModel:
        _user = self.db.query(User).filter(User.id == user_id).first()
        return _user

    def get_by_credentials(self, username: str, password: str) -> UserResponseModel:
        _user = self.db.query(User)\
            .filter(User.username == username) \
            .filter(User.password == password) \
            .first()
        return _user
