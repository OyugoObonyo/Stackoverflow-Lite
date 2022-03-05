"""
A module with views related to authorization and authentication
"""
from flask import current_app, render_template, redirect
from auth import bp
from auth.forms import RegistrationForm
from app.models.user import User
import


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    route that handles the user registration action
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
    return render_template('auth/register.html', title="Register", form=form)


@bp.route('/login')
def login():
    """
    route that handles user login action
    """
    return render_template('auth/login.html', title="Log In")
