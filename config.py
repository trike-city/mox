import os


class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-me'
    PG_USER = os.environ['PG_USER']
    PG_PASSWORD = os.environ['PG_PASSWORD']
    PG_HOST = os.environ['PG_HOST']
    PG_PORT = os.environ['PG_PORT']


class ProductionConfig(BaseConfig):
    DATABASE = 'mox_prod'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE = 'mox_dev'


class TestConfig(BaseConfig):
    TESTING = True
    DATABASE = 'mox_test'
