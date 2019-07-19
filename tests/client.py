import os
import tempfile
import pytest

from mox import create_app


@pytest.fixture
def client():
    db_fd, database_config = tempfile.mkstemp()

    app = create_app({
        'DATABASE': database_config,
        'TESTING': True
    })

    yield app.test_client()

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
