from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import User
from project.setup.api.models import user
from project.tools.security import auth_required


api = Namespace('user')


@api.route('/')
class UserView(Resource):

    @auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self) -> User:
        token = request.headers['Authorization'].split('Bearer ')[-1]
        return user_service.get_by_token(token)

    @auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def patch(self) -> User:
        token = request.headers['Authorization'].split('Bearer ')[-1]
        data = request.json
        return user_service.update(token, data)


@api.route('/password/')
class UserView(Resource):

    @auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def put(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        data = request.json
        return user_service.update_password(token, data)
