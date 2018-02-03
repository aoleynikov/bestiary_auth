from user import User
from users_repo import UsersRepo
import random


class UsersService:
    def __init__(self):
        self.repo = UsersRepo()

    def create(self, email, password):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+_)(*&^%$#@!"
        chars = []
        for i in range(16):
            chars.append(random.choice(alphabet))
        pass_salt = "".join(chars)
        user = User(email, '', pass_salt)
        user.pass_hash = user.hash_password(password)
        self.repo.create(user)

    def find(self, email):
        return self.repo.find(email)
