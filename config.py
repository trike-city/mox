import os


class BaseConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = 'change-me'
    PG_USER = os.environ['PG_USER']
    PG_PASSWORD = os.environ['PG_PASSWORD']
    PG_HOST = os.environ['PG_HOST']
    PG_PORT = os.environ['PG_PORT']

    @property
    def name(self):
        return self.NAME


class ProductionConfig(BaseConfig):
    NAME = 'production'
    DATABASE = 'mox_prod'


class DevelopmentConfig(BaseConfig):
    NAME = 'development'
    DEBUG = True
    DATABASE = 'mox_dev'


class TestConfig(BaseConfig):
    NAME = 'test'
    TESTING = True
    DATABASE = 'mox_test'


def for_key(key):
    switch = {
        'd': DevelopmentConfig,
        'dev': DevelopmentConfig,
        'development': DevelopmentConfig,
        'p': ProductionConfig,
        'prod': ProductionConfig,
        'production': ProductionConfig,
        't': TestConfig,
        'test': TestConfig,
        None: DevelopmentConfig,
        '': DevelopmentConfig
    }
    config_class = switch.get(key)

    if config_class is None:
        raise Exception(f'No config for key: {key}.')
    else:
        return config_class()
