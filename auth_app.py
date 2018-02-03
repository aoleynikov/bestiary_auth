from flask import Flask, request, Response
from users_service import UsersService
from tokens_service import TokensService
import re

app = Flask(__name__)


def validate(body):
    valid_email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", body.get('email', ''))
    return valid_email


@app.route('/health', methods=['GET'])
def healthcheck():
    return "Auth alive!"


@app.route('/register', methods=['POST'])
def register():
    body = request.get_json()
    if not validate(body):
        return Response(None, status=400)
    service = UsersService()
    conflict = service.find(body.get('email', ''))
    if conflict is not None:
        return Response(None, status=409)
    service.create(body.get('email'), body.get('password'))
    return Response(None, status=201)


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    service = TokensService()
    login_result = service.login(body.get('email', ''), body.get('password', ''))
    if login_result is None:
        return Response(None, status=401)
    else:
        return Response({'token': login_result}, status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
