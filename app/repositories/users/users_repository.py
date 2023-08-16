from sqlalchemy.orm import Session
from ...schemas import UserRequestModel, UserResponseModel
from typing import List
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: UserRequestModel, hash_password: str, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[UserResponseModel]:
        pass

    @abstractmethod
    def get(self, user_id: int, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def get_by_username(self, username: str, db: Session) -> UserResponseModel:
        pass
