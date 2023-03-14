from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_service
from project.setup.api.models import favorite
from project.tools.security import auth_required

api = Namespace('favorites')


@api.route('/movies/')
class FavoriteView(Resource):

    @auth_required
    @api.marshal_with(favorite, as_list=True, description='get all movies')
    def get(self):
        """
        get all

        """
        return favorite_service.get_all()


@api.route('/movies/<int:movie_id>/')
class FavoriteView(Resource):

    @auth_required
    @api.marshal_with(favorite, code=200, description='movie added')
    def post(self, movie_id: int):
        """
        Create new favorite movie in db
        :param movie_id:
        :return:
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        return favorite_service.add_movie(movie_id, token)

    @auth_required
    @api.marshal_with(favorite, code=204, description='movie deleted')
    def delete(self, movie_id: int):
        """
        Delete movie_id from table
        :param movie_id: int
        :return: None
        """
        return favorite_service.delete(movie_id)
