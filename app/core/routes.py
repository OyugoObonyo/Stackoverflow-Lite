"""
A module containing the application's index blueprint
"""
from flask import render_template
from app.core import bp


@bp.route('/')
def index():
    """
    route that renders the application's index template
    """
    return render_template('index.html', title="Home")
