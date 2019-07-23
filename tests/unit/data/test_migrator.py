import pytest

from mox.data import Migrator, Migration, Schema
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

    assert Schema(database).version == 2


def test_subsequent_migrate_latest(database):
    migrator = Migrator(database=database, dir_path=path)
    migrator.migrate_latest()
    migrator.migrate_latest()

    assert Schema(database).version == 2


def test_perform_migration(database):
    migrator = Migrator(database=database, dir_path=path)
    migration = Migration(path / '1_create_bad_decks.py')
    migrator.perform_migration(migration)

    table_exists = database.execute("""
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = 'bad_decks'
    );
    """)

    assert table_exists == [{'exists': True}]
    assert Schema(database).version == 1


def test_migrate_latest_when_some_migrations_have_been_performed(database):
    migrator = Migrator(database=database, dir_path=path)
    migration = Migration(path / '1_create_bad_decks.py')
    migrator.perform_migration(migration)
    migrator.migrate_latest()

    assert Schema(database).version == 2


def test_migrate_latest_returns_migrations(database):
    migrator = Migrator(database=database, dir_path=path)
    migrations = migrator.migrate_latest()
    names = [m.name for m in migrations]

    assert names == ['1_create_bad_decks', '2_add_name_to_bad_decks']
