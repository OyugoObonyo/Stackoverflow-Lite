"""
blueprint that handles routes and forms related to
authorization and authentication
"""
from flask import Blueprint

bp = Blueprint(__name__)

from app.auth import routes