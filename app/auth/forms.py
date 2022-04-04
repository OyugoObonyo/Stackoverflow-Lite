"""
Forms related to authorization and authentication
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):
    """
    Model of registration form
    """

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        """
        validate_username - checks that username entered doesn't already exist
        @username: username entered by user
        """
        pass

    def validate_email(self, email):
        """
        validate_email - checks that email enetered doesn't already exist
        @email: email entered by user
        """
        pass


class LoginForm(FlaskForm):
    """
    Model of login form
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")
