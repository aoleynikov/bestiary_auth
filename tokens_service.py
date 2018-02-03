from users_repo import UsersRepo
from jose import jwt
import os


class TokensService:
    def __init__(self):
        self.repo = UsersRepo()

    def login(self, login, password):
        user = self.repo.find(login)
        if user is None:
            return None
        h = user.hash_password(password)
        if h != user.pass_hash:
            return None
        return jwt.encode({'email': user.email}, os.environ['JWT_SECRET'])
