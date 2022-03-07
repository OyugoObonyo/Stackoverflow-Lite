"""
Fixtures for the pytest module
"""
from app import create_app
import os
import pytest


@pytest.fixture(scope="module")
def test_client():
    """
    creates an instance of flask application to be used
    """
    app = create_app()
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    # Establish an application context
    ctx = app.app_context()
    ctx.push()
    with app.test_client() as c:
        yield c
    ctx.pop()
