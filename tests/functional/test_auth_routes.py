"""
Module that tests the routes within the auth package
"""


def test_login_page_get(test_client):
    """
    GIVEN a login view function
    WHEN a user wants to GET the login page
    THEN render the login page
    """
    response = test_client.get('/auth/login')
    assert response.status_code == 200


def test_login_page_post(test_client):
    """
    GIVEN a login view function
    WHEN a user wants to POST to the login form
    THEN accept login form and redirect to index page when login is successful
    """
    response = test_client.post('/auth/login',
                                data=dict(
                                    username='te@mail.com',
                                    password='pas'),
                                follow_redirects=True)
    assert response.status_code == 200


def test_logout_page(test_client):
    """
    GIVEN a logout view function
    WHEN a user wants to logout of the application
    THEN log user out and redirect to index page
    """
    response = test_client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200


def test_register_page_get(test_client):
    """
    GIVEN a registration view function
    WHEN a user wants to access the registration page
    THEN render the registration page template
    """
    response = test_client.get('/auth/register')
    assert response.status_code == 200


def test_register_page_post(test_client):
    """
    GIVEN a registration view function
    WHEN a user wants to sign up to the application
    THEN render registration template, get user input and redirect to login
    """
    response = test_client.post('/auth/register',
                                data=dict(
                                    username='testuser',
                                    email='testuser@mail.com',
                                    password='password',
                                    password2='password'),
                                follow_redirects=True)
    assert response.status_code == 200
