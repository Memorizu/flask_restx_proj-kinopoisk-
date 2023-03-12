from project.config import BaseConfig
from project.dao.main import UserDAO
import jwt


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, user_id: int):
        user = self.dao.get_by_id(user_id)
        return user

    def create(self, data: dict):
        return self.dao.create(data)

    def get_by_email(self, email):
        user = self.dao.get_by_email(email)
        return user

    def get_by_token(self, token: bytes):
        user = jwt.decode(token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.ALGO)
        return self.dao.get_by_email_for_auth(user['email'])
