from utils import *
from flask import request, jsonify, abort, Blueprint
from bcrypt import hashpw, gensalt

print('**********************')
print('AUTH MODULE')

authapi = Blueprint('authapi', __name__)

# I simply care about getting THIS route to work, because the whole problem is getting routes to work that are
# in modules other than the main one (`application.py`)
@authapi.route("/test-auth/", methods=["GET"])
def test_auth():
    return jsonify({"data": "testing on auth page"})


@authapi.route("/login/", methods=["POST"])
def login():
    if (
        request.json["username"] == "demo"
        and request.json["password"] == "demo"
    ):
        return jsonify({"token": "12345"})
    abort(400)

@authapi.route("/api/me/", methods=["GET"])
@auth_required
def user_details():
    return jsonify({"username": "demo", "email": "demo@gmail.com"})


@authapi.route("/api/secure/", methods=["GET"])
@auth_required
def secure():
    hashed = hashpw('password'.encode('utf-8'), gensalt(rounds=13))
    print(hashed)

    if hashed == hashpw(b'password', hashed):
        print('oh it works')
    else:
        print('nope')
    return jsonify({"message": "this is fine"})
