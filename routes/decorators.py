from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.exceptions import JWTDecodeError
from werkzeug.exceptions import Unauthorized

def jwt_required_cookie(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            # Extract the JWT token from the HttpOnly cookie
            jwt_token = request.cookies.get('token')
            if not jwt_token:
                raise Unauthorized('Missing JWT token')
            # Verify the JWT token
            verify_jwt_in_request(jwt_token)
            # Call the decorated function
            return f(*args, **kwargs)
        except JWTDecodeError as e:
            raise Unauthorized('Invalid JWT token')
    return decorated
