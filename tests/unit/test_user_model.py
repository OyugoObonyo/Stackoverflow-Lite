"""
Module containing unit tests for the User model
"""
from app.models.user import User


def test_new_user():
    """
    GIVEN a User model,
    WHEN a new user is created,
    THEN check that all fields initialized with the user are correct
    """
    user = User(
        username='name',
        email="email@mail.com")
    assert user.username == 'name'
    assert user.email == 'email@mail.com'
    assert user.username != 'Name'
    assert user.email != 'email@gmail.com'
