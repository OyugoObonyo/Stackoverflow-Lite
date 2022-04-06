"""

routes that handle user authentication
"""

from app.auth import bp
from app.models.user import User
from app.models.sql_user_query_model import SqlUserQueryModel
from flask import request


@bp.route('/register', methods=['POST'])
def register():
    """
    
    register route handles user registration to the database
    """

    response = request.get_json()
    user = SqlUserQueryModel.get_by_name(response['username'])
    if user is None:
        user = User(
            username = response['username'],
            email = response['email'],
            password_hash = response['password'])
        SqlUserQueryModel.save(user)