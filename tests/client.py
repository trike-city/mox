import os
import tempfile
import pytest

from mox import create_app
from config import TestConfig


@pytest.fixture
def client():
    config = TestConfig()
    app = create_app(config)
    yield app.test_client()
