"""
A module containing the application's Config class
"""

import os


class Config:
    """
    The config class contains the application's default configurations
    """

    DB_HOST = 'localhost'
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    """
    Application's configurations during development
    """

    DB_NAME = os.environ.get('DB_DEV_NAME')
    DB_PASSWORD = os.environ.get('DB_DEV_PASSWORD')
    DB_USERNAME = os.environ.get('DB_DEV_USERNAME')


class TestingConfig(Config):
    """
    Application's configurations for testing
    """

    DB_NAME = os.environ.get('DB_TEST_NAME')
    DB_PASSWORD = os.environ.get('DB_TEST_PASSWORD')
    DB_USERNAME = os.environ.get('DB_TEST_USERNAME')
    TESTING = True


class ProductionConfig(Config):
    """
    Application's configurations during production
    """
    pass
