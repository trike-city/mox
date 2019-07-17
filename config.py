import os


class Config(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-me'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DATABASE_URL']


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URL']
