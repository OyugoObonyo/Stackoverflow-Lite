"""

routes that handle user authentication
"""

from base64 import decode
from app.auth import bp
from app.models.user import User
from app.models.sql_query_models.sql_user_query_model import SqlUserQueryModel
from flask import request
from utils.passwords import hashing
import datetime


@bp.route("/register", methods=["POST"])
def register():
    """

    register route handles user registration to the database
    """

    user_data = request.get_json()
    check_name = SqlUserQueryModel.get_by_name(user_data["username"])
    check_email = SqlUserQueryModel.get_by_email(user_data["email"])
    if check_name is None and check_email is None:
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            password_hash=hashing.generate_password_hash(user_data["password"]),
            created_at=datetime.datetime.utcnow(),
        )
        SqlUserQueryModel.save(user)
        response = {
            "status": "success",
            "account_information": {"name": user.username, "email": user.email},
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "A user with these credentials already exists",
        }
        return response


@bp.route("login", methods=["POST"])
def login():
    """
    
    handles user logins
    """

    user_data = request.get_json()
    user = SqlUserQueryModel.get_by_email(user_data["email"])
    if user is not None:
        if hashing.check_password_hash(user_data["password"], user.password_hash):
            token = user.generate_token(user.id)
            response = {"status": "success", "auth_token": token}
            return response
        response = {
            "status": "fail",
            "message": "Incorrect email and password combination",
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "A user with this email doesn't exist"
        }
        return response


@bp.route("logout", methods=["POST"])
def logout():
    """
    
    handles user logouts
    """
    auth_header = request.header.get('Authorization')
    print(f"auth_header: {auth_header}")
    auth_token = auth_header.split(" ")[1]
    if auth_token:
        decoded_token = User.decode_auth_token(auth_token)
        print(f"decoded token is: {decoded_token} and is of type {type(decoded_token)}")
        if not isinstance(decoded_token, str):



    