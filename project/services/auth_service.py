
from project.services.users_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create(self, data: dict):
        return self.user_service.create(data)

