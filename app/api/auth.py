from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from app.api.errors import error_response


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """verify_password"""
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    """basicauth"""
    return error_response(status)


@token_auth.verify_token
def verify_token(token):
    """verifytoken"""
    return User.checktoken(token) if token else None


@token_auth.error_handler
def token_auth(status):
    """tokenauth"""
    return error_response(status)
