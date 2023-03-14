from flask import request
from flask_restx import Namespace, Resource, abort

from project.container import auth_service


api = Namespace('auth')


@api.route('/register/')
class AuthView(Resource):

    def post(self):
        """
        New user registration
        :return: None
        """
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(401)

        return auth_service.create(data), 201


@api.route('/login/')
class AuthView(Resource):

    def post(self):
        """
        sign up by user
        :return: access and refresh tokens
        """
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(401)

        return auth_service.create_token(email, password), 200

    def put(self):
        """
        refreshing old tokens
        :return: new access and refresh tokens
        """
        token = request.json.get('refresh_token')
        tokens = auth_service.approve_token(token)
        return tokens, 200


