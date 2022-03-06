"""
Module that tests the routes within the auth package
"""


def test_login_page(test_client):
    """
    GIVEN a user wants to log in to their account
    WHEN a user fills in application form
    THEN render the login page
    """
    response = test_client.get('/auth/login')
    assert response.status_code == 200