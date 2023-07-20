from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    @classmethod
    def validate_username(cls, username: str) -> str:
        if len(username) < 4:
            raise ValueError('El username debe tener mínimo 4 caracteres')
        if len(username) > 50:
            raise ValueError('El username debe tener máximo 50 caracteres')

        return username

    class Config:
        schema_extra = {
            "example": {
                "username": 'Fernando',
                "password": "secret"
            }
        }


class UserResponseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
