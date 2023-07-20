from pydantic import BaseModel
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class MovieRequestModel(BaseModel):
    title: str


class MovieResponseModel(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
