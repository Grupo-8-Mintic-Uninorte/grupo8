from flask import redirect, request
from functools import wraps

def access(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if (request.endpoint == "home"):
            print("Estas en el home")
        return f(*args, **kws)
    return decorated_function
