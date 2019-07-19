import os


class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-me'


class ProductionConfig(BaseConfig):
    DATABASE = 'mox_prod'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE = 'mox_dev'


class TestConfig(BaseConfig):
    TESTING = True
    DATABASE = 'mox_test'
