from pymongo import MongoClient
from user import User

class UsersRepo:
    def __init__(self):
        client = MongoClient('mongo', 27017)
        self.collection = client.local['users']

    def create(self, user):
        self.collection.insert(user.__dict__)

    def find(self, email):
        doc = self.collection.find_one({'email': email})
        if doc is None:
            return None
        else:
            return User.from_document(doc)
