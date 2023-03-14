from project.dao.base import BaseDAO
from project.models import Favorite, User


class FavoriteDAO(BaseDAO):
    __model__ = Favorite

    def add_movie(self, user_email: str, movie_id: int):
        user = self.db_session.query(User).filter(User.email == user_email).first()
        favorite = Favorite(user_id=user.id, movie_id=movie_id)
        self.db_session.add(favorite)
        self.db_session.commit()
        return favorite

    def delete(self, movie_id: int):
        movie = self.db_session.query(Favorite).filter(Favorite.movie_id == movie_id).first()
        self.db_session.delete(movie)
        self.db_session.commit()

