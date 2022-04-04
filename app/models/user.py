"""
A module containing a data model of a user in the system
"""

from db.modify_db import run_sql


class User:
    """
    The user's data model
    """

    def __init__(
        self, username, email, password_hash=None, created_at=None, id=None
    ):
        """
        Initialzing the user class
        """
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.id = id
