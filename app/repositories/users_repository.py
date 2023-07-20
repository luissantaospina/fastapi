from ..models import User
from ..schemas import UserRequestModel, UserResponseModel
from sqlalchemy.orm import Session
from ..database import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session = get_db_session()):
        self.db = db

    def create(self, user: UserRequestModel, hash_password: str) \
            -> UserResponseModel:
        _user = User(username=user.username, password=hash_password)
        self.db.add(_user)
        self.db.commit()
        self.db.refresh(_user)
        return _user
