from ..helpers import encode_password
from ..repositories.users.impl import UserRepositoryImpl


class AuthService:
    @staticmethod
    def authenticate(username: str, password: str):
        _password = encode_password(password)
        _user = UserRepositoryImpl().get_by_credentials(username, _password)

        if _user:
            return _user
