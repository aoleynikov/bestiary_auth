import unittest
import json
from auth_app import app
from test_users_repo import TestUsersRepo


class AuthTest(unittest.TestCase):
    def setUp(self):
        self.repo = TestUsersRepo()
        self.client = app.test_client(self)

    def test_user_creation(self):
        email = 'mail@mail.com'
        response = self.client.post('/register',
                                    data=json.dumps({'email': email, 'password': '123'}),
                                    content_type='application/json')
        assert response.status_code == 201
        from_db = self.repo.find(email)
        assert from_db is not None

    def test_user_creation_with_invalid_email(self):
        email = 'mail'
        response = self.client.post('/register',
                                    data=json.dumps({'email': email, 'password': '123'}),
                                    content_type='application/json')
        assert response.status_code == 400
        from_db = self.repo.find(email)
        assert from_db is None

    def test_login_with_correct_data_returns_token(self):
        email = 'mail@mail.com'
        self.client.post('/register',
                         data=json.dumps({'email': email, 'password': '123'}),
                         content_type='application/json')
        response = self.client.post('/login',
                                    data=json.dumps({'email': email, 'password': '123'}),
                                    content_type='application/json')
        assert response.status_code == 200
        assert 'token' in str(response.data)

    def test_login_with_incorrect_data_returns_unauthorized(self):
        email = 'mail@mail.com'
        self.client.post('/register',
                         data=json.dumps({'email': email, 'password': '123'}),
                         content_type='application/json')
        response = self.client.post('/login',
                                    data=json.dumps({'email': email, 'password': 'wrong_password'}),
                                    content_type='application/json')
        assert response.status_code == 401
        assert len(response.data) == 0

    def tearDown(self):
        self.repo.delete_all()
