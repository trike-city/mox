import pytest

from mox.data import Migration
from pathlib import Path


path = Path('/user/src/mox/migrations/1_some_migration.py')


def test_name():
    assert Migration(path).name == '1_some_migration'


def test_version():
    assert Migration(path).version == 1


def test_path_str():
    assert Migration(path).path_str == '/user/src/mox/migrations/1_some_migration.py'
