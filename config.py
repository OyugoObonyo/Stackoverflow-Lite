"""
A module containing the application's Config class
"""
import os


class Config(object):
    """
    The config class contains the application's various configurations
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
