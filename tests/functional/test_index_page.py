"""
Tests for the app's index page
"""


def test_get_index_page(test_client):
    """
    GIVEN an index page view function,
    WHEN a user submits a GET request to that view function,
    THEN the login page shoould be successfully rendered
    """
    response = test_client.get('/')
    assert response.status_code == 200


def test_post_index_page(test_client):
    """
    GIVEN a user visits the application's homepage,
    WHEN the user wants to post data to the index page,
    THEN the application ought to render method not allowed error
    """
    response = test_client.post('/')
    assert response.status_code == 405
