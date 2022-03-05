"""
A module containing a data model of a user in the system
"""
from db.modify_db import run_sql
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    """
    The user's data model
    """
    def __init__(self, id, created_at, username, email, password_hash):
        """
        Initialzing the user class
        """
        self.id = id
        self.created_at = created_at
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def set_password(self, password):
        """
        set_password - generates a password hash from users' passwords
        @password: password to be hashed
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        check_password - confirms a hash is assigned to the correct password
        Returns: True if the hash matches the password and false if it doesn't
        """
        return check_password_hash(self.password_hash, password)

    def save(self):
        """
        Saves the particlar user to the database
        """
        sql = """
            INSERT INTO users(
                id,
                created_at,
                username,
                email,
                password_hash') VALUES (%s, %s, %s, %s)
            """
        val = [self.created_at, self.username, self.email, self.password_hash]
        run_sql(sql, val)
