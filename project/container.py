from project.dao import GenresDAO
from project.dao.main import MoviesDAO

from project.services import GenresService
from project.services.movie_service import MovieService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
