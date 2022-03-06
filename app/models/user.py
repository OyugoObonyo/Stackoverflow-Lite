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
    def __init__(self, username):
        """
        Initialzing the user class
        """
        self.username = username
        self.email = ""
        self.password_hash = ""
        self.created_at = ""

    def set_password(self, password):
        """
        set_password - generates a password hash from users' passwords
        @password: password to be hashed
        """
        self.password_hash = generate_password_hash(password)

    def check_password(password_hash, password):
        """
        check_password - confirms a hash is assigned to the correct password
        Returns: True if the hash matches the password and false if it doesn't
        """
        return check_password_hash(password_hash, password)

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

    def get_by_id(id):
        """
        get_by_id - retrives a user of a particular id from database
        @id: the id passed as integer
        Returns: user with passed id
        """
        sql = "SELECT * FROM users WHERE id = %s"
        value = [id]
        result = run_sql(sql, value)[0]
        return result['id']

    def get_by_name(name):
        """
        get_by_name - retireves user with a particular name from the database
        @name: name of the user to be retrieved
        Returns: user who matches the name that is passed
        """
        sql = "SELECT * FROM users WHERE username = %s"
        value = [name]
        result = run_sql(sql, value)[0]
        return result


@login.user_loader
def load_user(id):
    """
    load_user - aids flask in geting user id for login
    Returns: user with particular id
    """
    return User.get_by_id(id)
