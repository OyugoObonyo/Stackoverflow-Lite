"""

routes that handle user authentication
"""


from crypt import methods
from app.auth import bp
from app.models.user import User
from app.models.sql_user_query_model import SqlUserQueryModel
from flask import make_response, request
from utils.passwords import hashing
import bcrypt
import datetime


@bp.route("/register", methods=["POST"])
def register():
    """

    register route handles user registration to the database
    """

    response = request.get_json()
    check_name = SqlUserQueryModel.get_by_name(response["username"])
    check_email = SqlUserQueryModel.get_by_email(response["email"])
    if check_name is None and check_email is None:
        user = User(
            username=response["username"],
            email=response["email"],
            password_hash=hashing.generate_password_hash(response["password"]),
            created_at=datetime.datetime.utcnow()
        )
        SqlUserQueryModel.save(user)
        response = {
            "status": "success",
            "account_information": {
                "name": user.username,
                "email": user.email
            }
        }
        return make_response(response), 201
    else:
        response = {
            "status": "fail",
            "message": "A user with these credentials already exists"
        }
        return make_response(response), 400

    
@bp.route("login", methods=["POST"])
def login():
    """
    
    handles user logins
    """

    response = request.get_json()
    user = SqlUserQueryModel.get_by_email(response['email'])
    if user is not None:
        if bcrypt.checkpw(response['password'], user.password_hash):
            response = {
                "status": "success",
                "token": 
            }

        
