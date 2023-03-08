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

    def get_all(self, status: Optional[str] = None,
                page: Optional[int] = None):
        super().get_all()
        stmt = self._db_session.query(self.__model__)
        if page:
            try:
                return BaseDAO.get_all(self, page)
            except NotFound:
                return []
        if status:
            try:
                return self._db_session.query(self.__model__).order_by(-self.__model__.year).all()
            except NotFound:
                return []
        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User
