from flask_restx import abort

from project.config import BaseConfig
from project.dao.main import UserDAO
import jwt
from project.tools.security import generate_password_hash

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

    def get_by_token(self, token):
        user = jwt.decode(token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.ALGO)
        return self.dao.get_by_email(user['email'])

    def update(self, token, data):
        user = self.get_by_token(token)
        if 'email' in data:
            user.email = data.get('email')
        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')
        if 'favorite_movie' in data:
            user.favorite_movie = data.get('favorite_movie')

        return self.dao.update(user)

    def update_password(self, token, data):
        user = self.get_by_token(token)
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        if user.password != generate_password_hash(old_password):
            abort(401)
        user.password = generate_password_hash(new_password)

        return self.dao.update(user)
