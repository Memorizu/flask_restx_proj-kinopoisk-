from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service

api = Namespace('auth')


@api.route('/register')
class AuthView(Resource):

    def post(self):
        data = request.json
        return auth_service.create(data)

