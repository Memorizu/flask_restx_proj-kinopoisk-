import base64
import hashlib
import hmac
from typing import Union
from flask import request
from flask import abort
import jwt

from project.config import BaseConfig
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    """
    convert password to bytes
    :param password: str
    """
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    """
    convert password to hash
    :param password: str
    """
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compose_passwords(password_hash: Union[str, bytes], password: str):
    """
    compare passwords
    """
    decode_password = base64.b64decode(password_hash)

    hash_password = __generate_password_digest(password)
    return hmac.compare_digest(decode_password, hash_password)


def auth_required(func):
    def wrapper(*args, **kwargs):
        """
        Checking headers, if user is authorizing,
        will decode his token
        """
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper
