from typing import Optional

from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.models import Genre, User
from project.models import Director
from project.models import Movie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_by_status(self, status: Optional[str] = None,
                          page: Optional[int] = None):
        """
        get all movies, Optionally can be argument status and page
        :param status: str
        :param page: int
        :return: all movies
        """
        stmt = self._db_session.query(Movie)
        if status:
            if status == 'new':
                stmt = stmt.order_by(-Movie.year)

        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []

        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, data: dict):
        new_user = User(**data)
        self.db_session.add(new_user)
        self.db_session.commit()

    def get_by_email(self, email: str):
        user = self.db_session.query(User).filter(User.email == email).first()
        return user

    def update(self, user: dict):
        self.db_session.add(user)
        self.db_session.commit()
        return user


