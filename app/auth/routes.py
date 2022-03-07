"""
A module with views related to authorization and authentication
"""
from flask import current_app, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm
from app.models.user import User
import datetime


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    route that handles the user registration action
    """
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.created_at = datetime.datetime.now()
        user.save()
        flash("You have successfully signed up")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title="Register", form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    route that handles user login action
    """
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_name(form.username.data)
        if user is None or not \
                User.check_password(user.password_hash, form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('core.index'))
    return render_template('auth/login.html', title="Log In", form=form)


@bp.route('/logout')
def logout():
    """
    Route that handles logging users out
    """
    logout_user()
    return redirect(url_for('core.index'))
