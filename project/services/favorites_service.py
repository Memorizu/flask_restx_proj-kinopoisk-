import jwt

from project.config import BaseConfig
from project.dao import UserDAO
from project.dao.favorite import FavoriteDAO
from project.tools.security import auth_required


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def add_movie(self, movie_id, token):
        user = jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.ALGO)
        return self.dao.add_movie(user['email'], movie_id)

    def delete(self, movie_id: int):
        return self.dao.delete(movie_id)
