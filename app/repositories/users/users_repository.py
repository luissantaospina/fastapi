from ...schemas import UserRequestModel, UserResponseModel
from typing import List
from ...database import get_db_session
from abc import ABC, abstractmethod

db_dependency = next(get_db_session())


class UserRepository(ABC):
    def __init__(self):
        self.db = db_dependency

    @abstractmethod
    def create(self, user: UserRequestModel, hash_password: str) -> UserResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int = 1, limit: int = 10) -> List[UserResponseModel]:
        pass

    @abstractmethod
    def get(self, user_id: int) -> UserResponseModel:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserResponseModel:
        pass
