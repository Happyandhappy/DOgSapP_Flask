import functools
from flask import request, abort

def auth_required(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if request.headers.get("Authorization") == "Bearer 12345":
            return fn(*args, **kwargs)
        else:
            abort(401)

    return wrapper
