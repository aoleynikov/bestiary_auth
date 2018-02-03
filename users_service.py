from user import User
from users_repo import UsersRepo
from password_hasher import hash_password
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
        pass_hash = hash_password(password, pass_salt)
        user = User(email, pass_hash, pass_salt)
        self.repo.create(user)

    def find(self, email):
        return self.repo.find(email)
