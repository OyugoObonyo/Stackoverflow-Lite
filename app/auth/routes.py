"""
A module with views related to authorization and authentication
"""
from flask import current_app, render_template, redirect
from app.auth import bp
from app.auth.forms import RegistrationForm
from app.models.user import User
import datetime


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
        user.set_password(form.password.data)
        time = datetime.datetime.now()
        user.created_at = time
        user.save()
    return render_template('auth/register.html', title="Register", form=form)


@bp.route('/login')
def login():
    """
    route that handles user login action
    """
    return render_template('auth/login.html', title="Log In")
