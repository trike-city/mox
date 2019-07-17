import os
import tempfile
import pytest

from mox import create_app
from config import TestConfig


@pytest.fixture
def client():
    app = create_app(TestConfig)
    yield app.test_client()
