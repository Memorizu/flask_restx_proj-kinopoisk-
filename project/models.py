from sqlalchemy import Column, String, Integer, Float

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(200))
    description = Column(String())
    trailer = Column(String())
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer())
    director_id = Column(Integer())


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(), unique=True, nullable=False)


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String(150))
    surname = Column(String(200))
    favorite_genre = Column(String())

