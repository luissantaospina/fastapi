import hashlib


def encode_password(password: str) -> str:
    hash_lib = hashlib.md5()
    hash_lib.update(password.encode('utf-8'))
    return hash_lib.hexdigest()
