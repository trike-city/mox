import pytest

from tests.fixtures import database
from mox.data import Schema


def test_create_if_needed(database):
    schema = Schema(database)
    schema.create_if_needed()
    versions = database.execute('select (version) from schema_versions;')

    assert versions == [{'version': 0}]


def test_version_getter(database):
    schema = Schema(database)
    schema.create_if_needed()

    assert schema.version == 0


def test_version_setter(database):
    schema = Schema(database)
    schema.create_if_needed()
    schema.version = 2
    versions = database.execute('select (version) from schema_versions;')

    assert versions == [{'version': 0}, {'version': 2}]
