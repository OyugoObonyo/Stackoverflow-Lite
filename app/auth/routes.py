"""
A module with views related to authorization and authentication
"""
from crypt import methods
from flask import current_app, render_template, redirect
from app.auth import bp


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    route that handles the user registration action
    """
    pass


@bp.route('/login')
def login():
    """
    route that handles user login action
    """
    pass