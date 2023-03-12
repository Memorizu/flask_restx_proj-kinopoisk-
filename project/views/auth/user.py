from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import User
from project.tools.security import auth_required


api = Namespace('user')


@api.route('/')
class UserView(Resource):

    @auth_required
    def get(self, user_id: int) -> User:
        return user_service.get_one(user_id)

    @auth_required
    def patch(self, user_id: int) -> User:
        pass


@api.route('/password')
class UserView(Resource):

    @auth_required
    def put(self, user_id: int, password: str):
        pass