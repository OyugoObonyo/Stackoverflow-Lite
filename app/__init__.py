"""
A module containing a factory function to initialize the application
"""
from flask import Flask
from config import Config
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


def create_app(config_class=Config):
    """
    create_app - factory function which creates application instance
    @config_class: configuration variables of the application
    Returns: an application instance object
    """
    return app
