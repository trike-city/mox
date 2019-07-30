import os
import tempfile
import pytest

from config import TestConfig


@pytest.fixture
def client():
    from mox import create_app
    config = TestConfig()
    app = create_app(config)
    yield app.test_client()


@pytest.fixture
def database():
    from mox.data import Database
    config = TestConfig()
    db = Database(config)
    db.open()
    yield db
    db.rollback()
    db.close()
