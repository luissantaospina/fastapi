from pydantic import BaseModel, validator, Field


class ReviewRequestModel(BaseModel):
    movie_id: int
    review: str = Field(max_length=50, min_length=5)
    score: int = Field(le=5, ge=1)

    class Config:
        schema_extra = {
            "example": {
                "movie_id": 1,
                "review": "The movie was fine",
                "score": 4
            }
        }


class ReviewRequestPutModel(BaseModel):
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


class ReviewResponseModel(BaseModel):
    id: int
    review: str
    score: float

    class Config:
        orm_mode = True
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
