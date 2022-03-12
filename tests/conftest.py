"""
Fixtures for the pytest module
"""
from app import create_app
import os
import psycopg2
import pytest
import psycopg2.extras as ext


@pytest.fixture(scope="module")
def test_client():
    """
    creates an instance of flask application to be used
    """
    app = create_app('testing')
    # Establish an application context
    ctx = app.app_context()
    ctx.push()
    with app.test_client() as c:
        yield c
    ctx.pop()


@pytest.fixture(scope="session")
def setup_db():
    """
    creates a database connection
    """
    conn = psycopg2.connect(
            host="localhost",
            database="test_stackoverflow",
            user="test_stack",
            password="password",
            sslmode='require')
    cur = conn.cursor(cursor_factory=ext.DictCursor)
    yield cur0
    cur.execute(sql, values)
    conn.commit()
    results = cur.fetchall()
    cur.close()