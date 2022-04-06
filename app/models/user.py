"""

A module containing a data model of a user in the system
"""

from db.modify_db import run_sql
from flask import current_app
import datetime
import jwt


class User:
    """

    The user's data model
    """

    def __init__(self, username, email, password_hash=None, created_at=None, id=None):
        """

        Initialzing the user class
        """

        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.id = id

    def get_token(self, user_id):
        """ "

        get_token generates a token for a user to be used for authentication
        :user_id: id of user whose token is to be generated
        :return: token
        """

        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=0, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(
                payload, current_app.config["SECRET_KEY"], algorithm="HS256"
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        decode_auth_token decodes the auth token passed to it
        :auth_token: the token to be decoded
        :return: id of user associated with the token or an error string
        """
        try:
            payload = jwt.decode(auth_token, current_app.config("SECRET_KEY"))
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
