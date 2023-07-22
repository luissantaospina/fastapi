from pydantic import BaseModel


class MovieRequestModel(BaseModel):
    title: str

    class Config:
        schema_extra = {
            "example": {
                "title": 'Interestelar'
            }
        }


class MovieResponseModel(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
