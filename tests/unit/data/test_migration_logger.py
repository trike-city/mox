import pytest

from config import DevelopmentConfig
from pathlib import Path
from mox.data import MigrationLogger, Migration


class MockOutput:
    def __init__(self):
        self.value = None

    def log(self, value):
        self.value = value


def test_output_with_migrations():
    output = MockOutput()
    logger = MigrationLogger(out=output, config=DevelopmentConfig())

    logger.log_performed_migrations([
        Migration(Path('/test/1_create_animals.py')),
        Migration(Path('/test/2_add_name_to_animals.py'))
    ])

    assert output.value == 'Environment: development\n' \
                           'Performed 2 migrations:\n' \
                           '/test/1_create_animals.py\n' \
                           '/test/2_add_name_to_animals.py'


def test_output_with_single_migrations():
    output = MockOutput()
    logger = MigrationLogger(out=output, config=DevelopmentConfig())
    logger.log_performed_migrations([Migration(Path('/test/1_create_animals.py'))])

    assert output.value == 'Environment: development\n' \
                           'Performed 1 migration:\n' \
                           '/test/1_create_animals.py'
