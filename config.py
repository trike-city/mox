import os


class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-me'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ['PROD_DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DATABASE_URL']


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URL']
