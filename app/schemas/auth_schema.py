from pydantic import ConfigDict, BaseModel
from app.schemas import UserResponseModel


class AuthResponseModel(BaseModel):
    access_token: str
    token_type: str
    user: UserResponseModel
    model_config = ConfigDict(from_attributes=True)
