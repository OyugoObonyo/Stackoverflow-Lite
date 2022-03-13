"""
Module containing unit tests for the User model
"""


def test_new_user(new_user):
    """
    GIVEN a User model,
    WHEN a new user is created,
    THEN check that all fields initialized with the user are correct
    """

    assert new_user.username == 'name'
    assert new_user.email == 'email@mail.com'
    assert new_user.username != 'Name'
    assert new_user.email != 'email@gmail.com'


def test_user_password_hashing(new_user):
    """
    GIVEN a user's password
    WHEN a user passes their password,
    THEN hash the user's password and save it as  a user's password
    """

    new_user.set_password('password')
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(new_user.username)
    print(new_user.email)
    print(new_user.password_hash)
    print(new_user.id)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    assert new_user.check_password('password') is True
    assert new_user.check_password('passsword') is False
