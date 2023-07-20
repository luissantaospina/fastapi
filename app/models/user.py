from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import hashlib

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    reviews = relationship('Review')

    def __str__(self):
        return self.username

    @classmethod
    def create_password(cls, password: str) -> str:
        hash_lib = hashlib.md5()
        hash_lib.update(password.encode('utf-8'))
        return hash_lib.hexdigest()

    @classmethod
    def authenticate(cls, username: str, password: str):
        password = User.create_password(password)
        user = cls.select() \
            .where(User.username == username) \
            .where(User.password == password) \
            .first()

        if user:
            return user
