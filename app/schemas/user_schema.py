from pydantic import field_validator, ConfigDict, BaseModel


class UserRequestModel(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, username: str) -> str:
        if len(username) < 4:
            raise ValueError('El username debe tener mínimo 4 caracteres')
        if len(username) > 50:
            raise ValueError('El username debe tener máximo 50 caracteres')

        return username
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "username": 'luis',
            "password": "luis"
        }
    })


class UserResponseModel(BaseModel):
    id: int
    username: str
    is_activate: bool
    model_config = ConfigDict(from_attributes=True)
