"""
A module containing a factory function to initialize the application
"""
from flask import Flask
from config import Config
from dotenv import load_dotenv


def create_app(config_class=Config):
    """
    create_app - factory function which creates application instance
    @config_class: configuration variables of the application
    Returns: an application instance object
    """
    app = Flask(__name__)
    # attach the configuration variables from the application
    app.config.from_object(Config)
    load_dotenv()

    from app.core import bp as core_bp
    app.register_blueprint(core_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    return app
