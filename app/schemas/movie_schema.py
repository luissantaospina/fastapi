from pydantic import ConfigDict, BaseModel


class MovieRequestModel(BaseModel):
    title: str
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "title": 'Interestelar'
        }
    })


class MovieResponseModel(BaseModel):
    id: int
    title: str
    model_config = ConfigDict(from_attributes=True)
