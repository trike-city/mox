import pytest

from mox.data import Migrator
from tests.fixtures import database
from pathlib import Path


path = Path().absolute() / 'tests/unit/data/migrations'


def test_migrate_latest_performs_migrations(database):
    migrator = Migrator(database=database, dir_path=path)
    migrator.migrate_latest()
    database.execute('INSERT INTO bad_decks (name) VALUES (\'horse tribal\');')
    result = database.execute('SELECT * FROM bad_decks;')

    assert result == [{'name': 'horse tribal'}]


def test_migrate_latest_persists_schema_version(database):
    migrator = Migrator(database=database, dir_path=path)
    migrator.migrate_latest()
    result = database.execute('SELECT * FROM schema_versions;')

    assert result == [{'version': 2}]


def test_migrate_latest_when_schema_versions_table_already_exits(database):
    database.execute('CREATE TABLE schema_versions (version INT);')

    migrator = Migrator(database=database, dir_path=path)
    migrator.migrate_latest()
    result = database.execute('SELECT * FROM schema_versions;')

    assert result == [{'version': 2}]
