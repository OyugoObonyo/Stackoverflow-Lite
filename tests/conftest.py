"""
Fixtures for the pytest module
"""

from app import create_app
from app.models.user import User
from config import TestingConfig
import pytest


@pytest.fixture(scope="module")
def test_client():
    """
    creates an instance of flask application to be used
    """
    app = create_app(config_class=TestingConfig)
    app.config['SECRET_KEY'] = "secret-key-test"
    ctx = app.app_context()
    ctx.push()
    with app.test_client() as c:
        yield c
    ctx.pop()


@pytest.fixture(scope="module")
def new_user():
    """
    creates a user object to be used across the application
    """
    user = User(
        username='name',
        email="email@mail.com")
    return user
