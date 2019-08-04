from .migration import Migration
from .schema import Schema
from pathlib import Path


__migration_path__ = Path().absolute() / 'mox/data/migrations'


class Migrator:
    def __init__(self, database, dir_path=__migration_path__):
        self.database = database
        self.dir_path = dir_path
        self.schema = Schema(database)

    def migrate_latest(self):
        self.schema.create_if_needed()
        migrations = self.__find_pending_migrations()

        if len(migrations) > 0:
            self.__perform_migrations(migrations)
            self.schema.version = migrations[-1].version

        return migrations

    def perform_migration(self, migration):
        self.schema.create_if_needed()
        migration.up(self.database)
        self.schema.version = migration.version

    def __find_pending_migrations(self):
        file_paths = [f for f in self.dir_path.glob('**/*') if f.is_file()]
        migrations = [Migration(path) for path in file_paths]
        pending_migrations = [m for m in migrations if m.version > self.schema.version]
        return self.__sort_by_versions(pending_migrations)

    def __sort_by_versions(self, migrations):
        def version(migration):
            return migration.version

        return sorted(migrations, key=version)

    def __perform_migrations(self, migrations):
        for m in migrations:
            m.up(self.database)
