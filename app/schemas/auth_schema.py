from pydantic import BaseModel
from app.schemas import UserResponseModel


class AuthResponseModel(BaseModel):
    access_token: str
    token_type: str
    user: UserResponseModel

    class Config:
        orm_mode = True
