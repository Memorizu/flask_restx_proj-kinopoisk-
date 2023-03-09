import base64
import hashlib

from project.config import BaseConfig
from project.dao.base import BaseDAO
from project.models import User


class UserService:
    def __init__(self, dao: BaseDAO[User]):
        self.dao = dao

    def get_one(self, user_id: int):
        user = self.dao.get_by_id(user_id)
        return user

    def create(self, data):
        new_user = User(**data)
        self.dao.db_session.add(new_user)
        self.dao.db_session.commit()


