import pytest
import config


def test_for_key_returns_dev():
    assert config.for_key('d').name == 'development'
    assert config.for_key('dev').name == 'development'
    assert config.for_key('development').name == 'development'


def test_for_key_returns_prod():
    assert config.for_key('p').name == 'production'
    assert config.for_key('prod').name == 'production'
    assert config.for_key('production').name == 'production'


def test_for_key_returns_test():
    assert config.for_key('t').name == 'test'
    assert config.for_key('test').name == 'test'


def test_for_key_default_value():
    assert config.for_key(None).name == 'development'
    assert config.for_key('').name == 'development'


def test_wrong_value():
    with pytest.raises(Exception):
        assert config.for_key('jambon')
