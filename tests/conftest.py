"""
Fixtures for the pytest module
"""
import pytest
from app import create_app


@pytest.fixture(scope="module")
def test_client():
    """
    creates an instance of flask application to be used
    """
    app = create_app()
    with app.test_client() as c:
        yield c
