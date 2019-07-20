import pytest

from mox.data import Migration
from pathlib import Path


def test_name():
    path = Path('/user/src/mox/migrations/1_some_migration.py')
    migration = Migration(path)

    assert migration.name == '1_some_migration'
