import pytest

from mox.data import Migrator
from mox.data import Migration
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


def test_perform_migration(database):
    migrator = Migrator(database=database, dir_path=path)
    migration = Migration(path / '1_create_bad_decks.py')
    migrator.perform_migration(migration)

    versions = database.execute('SELECT * FROM schema_versions;')
    table_exists = database.execute("""
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = 'bad_decks'
    );
    """)

    assert versions == [{'version': 1}]
    assert table_exists == [{'exists': True}]
