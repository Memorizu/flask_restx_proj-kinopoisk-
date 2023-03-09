
from project.services.users_service import UserService
from project.tools.security import generate_password_hash

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create(self, data: dict):
        hash_pass = generate_password_hash(data['password'])
        data['password'] = hash_pass
        return self.user_service.create(data)

    def create_token(self, data: dict):
