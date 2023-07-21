from pydantic import BaseModel


class MovieRequestModel(BaseModel):
    title: str


class MovieResponseModel(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
