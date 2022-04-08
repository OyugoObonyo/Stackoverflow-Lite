"""

The sql_query_user module: Contains SqlUserQueryModel class

This module demonstrates implementation of SqlUserQueryModel class that is
useful in querying the database's user table
"""

from app.models.abstract_user_query import AbtsractUserQueryModel
from utils.db import modify_db
from user import User


class SqlUserQueryModel(AbtsractUserQueryModel):
    """

    SqlUserQueryModel handles queries to SQL databases

    SqlUserQueryModel objects is tasked with writing queries to SQL-based
    databases
    """

    def save(user):
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
        val = [user.created_at, user.username, user.email, user.password_hash]
        modify_db.run_sql(sql, val)

    def get_by_id(id):
        """

        get_by_id - retrives a user of a particular id from database
        @id: the id passed as integer
        Returns: user with passed id
        """

        sql = "SELECT * FROM users WHERE id = %s"
        value = [id]
        try:
            result = modify_db.run_sql(sql, value)[0]
            user = User(
                id=result["id"],
                created_at=result["created_at"],
                username=result["username"],
                email=result["email"],
                password_hash=result["password_hash"],
            )
        except IndexError:
            return None
        return user

    def get_by_name(name):

        """
        get_by_name - retireves user with a particular name from the database
        @name: name of the user to be retrieved
        Returns: user who matches the name that is passed
        """

        sql = "SELECT * FROM users WHERE username = %s"
        value = [name]
        try:
            result = modify_db.run_sql(sql, value)[0]
            user = User(
                id=result["id"],
                created_at=result["created_at"],
                username=result["username"],
                email=result["email"],
                password_hash=result["password_hash"],
            )
        except IndexError:
            return None
        return user
