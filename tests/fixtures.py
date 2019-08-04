import os
import tempfile
import pytest

from config import TestConfig


@pytest.fixture
def client():
    from mox import create_app, Dependencies

    config = TestConfig()
    deps = Dependencies(config)
    client = create_app(deps).test_client()
    client.database = deps.database

    yield client

    deps.database.rollback()
    deps.database.close()


@pytest.fixture
def database():
    from mox.data import Database
    config = TestConfig()
    db = Database(config)
    db.open()
    yield db
    db.rollback()
    db.close()
