"""
A module containing a data model of a user in the system
"""
from app import login
from db.modify_db import run_sql
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    """
    The user's data model
    """
    def __init__(self, username, email):
        """
        Initialzing the user class
        """
        self.username = username
        self.email = email
        self.password_hash = ""
        self.created_at = ""

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
                created_at,
                username,
                email,
                password_hash) VALUES (%s, %s, %s, %s) RETURNING id
            """
        val = [self.created_at, self.username, self.email, self.password_hash]
        results = run_sql(sql, val)

    def get_by_id(self, id):
        """
        get_by_id - retrives a user of a particular id from database
        @id: the id passed as integer
        Returns: user id
        """
        sql = "SELECT * FROM users WHERE id = %s"
        val = [id]
        result = run_sql(sql, val)[0]
        return result


@login.user_loader
def load_user(id):
    """
    load_user - aids flask in geting user id for login
    Returns: user with particular id
    """
    return User.get_by_id(id)
