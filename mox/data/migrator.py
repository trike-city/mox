from .migration import Migration
from .schema import Schema


class Migrator:
    def __init__(self, database, dir_path):
        self.database = database
        self.dir_path = dir_path
        self.schema = Schema(database)
        self.schema.create_if_needed()

    def migrate_latest(self):
        migrations = self.__find_pending_migrations()

        if len(migrations) > 0:
            self.__perform_migrations(migrations)
            self.schema.version = migrations[-1].version

    def perform_migration(self, migration):
        migration.up(self.database)
        self.schema.version = migration.version

    def __find_pending_migrations(self):
        file_paths = [f for f in self.dir_path.glob('**/*') if f.is_file()]
        migrations = [Migration(path) for path in file_paths]
        migrations.reverse()
        return [m for m in migrations if m.version > self.schema.version]

    def __perform_migrations(self, migrations):
        for m in migrations:
            m.up(self.database)
