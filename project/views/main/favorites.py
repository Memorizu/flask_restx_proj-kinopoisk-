from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_service
from project.setup.api.models import favorite
from project.tools.security import auth_required

api = Namespace('favorites')


@api.route('/movies/')
class FavoriteView(Resource):

    @auth_required
    @api.marshal_with(favorite)
    def get(self):
        return favorite_service.get_all()


@api.route('/movies/<int:movie_id>/')
class FavoriteView(Resource):

    @auth_required
    @api.marshal_with(favorite, code=200, description='movie added')
    def post(self, movie_id: int):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        return favorite_service.add_movie(movie_id, token)

    @auth_required
    @api.marshal_with(favorite, code=204, description='movie deleted')
    def delete(self, movie_id: int):
        favorite_service.delete(movie_id)
        return ''
