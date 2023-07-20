from pydantic import BaseModel, validator, Field
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect
from .movie import MovieResponseModel


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class UserReviewRequestModel(BaseModel):
    movie_id: int
    review: str = Field(max_length=50, min_length=5)
    score: int = Field(le=5, ge=1)

    class Config:
        # Add example to schema
        schema_extra = {
            "example": {
                "movie_id": 1,
                "review": "The movie was fine",
                "score": 4
            }
        }


class UserReviewRequestPutModel(BaseModel):
    review: str
    score: float

    # custom validation
    @validator('score')
    @classmethod
    def validate_score(cls, score: float) -> float:
        if score < 1:
            raise ValueError('El score debe ser mayor o igual a 1')
        if score > 5:
            raise ValueError('El score debe ser menor o igual a 5')

        return score


class UserReviewResponseModel(BaseModel):
    id: int
    movie: MovieResponseModel
    review: str
    score: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        # Add example to schema
        schema_extra = {
            "example": {
                "id": 1,
                "movie": {
                    "id": 1,
                    "title": "titanic"
                },
                "review": "The movie was fine",
                "score": 4
            }
        }
