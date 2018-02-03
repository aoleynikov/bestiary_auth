import hashlib


class User:
    def __init__(self, email, pass_hash, pass_salt):
        self.email = email
        self.pass_hash = pass_hash
        self.pass_salt = pass_salt

    def from_document(document):
        return User(document.get('email', None),
                    document.get('pass_hash', None),
                    document.get('pass_salt', None))

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8') + self.pass_salt.encode('utf-8')).hexdigest()

