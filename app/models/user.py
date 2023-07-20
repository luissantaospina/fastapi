from peewee import Model, CharField, DateTimeField
from datetime import datetime
from .database import database
import hashlib


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

    @classmethod
    def create_password(cls, password: str) -> str:
        hash_lib = hashlib.md5()
        hash_lib.update(password.encode('utf-8'))
        return hash_lib.hexdigest()

    @classmethod
    def authenticate(cls, username: str, password: str):
        password = User.create_password(password)
        user = cls.select()\
            .where(User.username == username) \
            .where(User.password == password) \
            .first()

        if user:
            return user
