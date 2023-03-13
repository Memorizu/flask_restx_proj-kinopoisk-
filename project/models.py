from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

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
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    genre = relationship('Genre')
    director_id = Column(Integer(), ForeignKey('directors.id'))
    director = relationship('Director')


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(200), unique=True, nullable=False)


class Favorite(models.Base):
    __tablename__ = 'favorites'

    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    user = relationship('User')
    movie_id = Column(Integer(), ForeignKey('movies.id'), nullable=False)
    movie = relationship('Movie')


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String(150))
    surname = Column(String(200))
    favorite_genre = Column(Integer(), ForeignKey('genres.id'))
    genre = relationship('Genre')
    favorite_movie = Column(Integer(), ForeignKey('movies.id'))
    movie = relationship('Movie')
