from .migration import Migration
from datetime import datetime


class Migrator:
    def __init__(self, database, dir_path):
        self.database = database
        self.dir_path = dir_path

    def migrate_latest(self):
        self.__create_schema_versions_table_if_needed()
        migrations = self.__find_pending_migrations()

        if len(migrations) > 0:
            self.__perform_migrations(migrations)
            self.__store_new_version(migrations[-1])

    def perform_migration(self, migration):
        migration.up(self.database)
        self.__create_schema_versions_table_if_needed()
        self.__store_new_version(migration)

    def __create_schema_versions_table_if_needed(self):
        self.database.execute("""
        CREATE TABLE IF NOT EXISTS schema_versions (
            version INT,
            created_at TIMESTAMP NOT NULL
        );
        """)

    def __find_pending_migrations(self):
        schema_version = self.__find_current_version()
        file_paths = [f for f in self.dir_path.glob('**/*') if f.is_file()]
        migrations = [Migration(path) for path in file_paths]
        migrations.reverse()
        return [m for m in migrations if m.version > schema_version]

    def __perform_migrations(self, migrations):
        for m in migrations:
            m.up(self.database)

    def __store_new_version(self, migration):
        sql = 'INSERT INTO schema_versions (version, created_at) VALUES (%s, %s);'
        self.database.execute(sql, (migration.version, datetime.now()))

    def __find_current_version(self):
        result = self.database.execute("""
        SELECT (version)
        FROM schema_versions
        ORDER BY created_at DESC
        LIMIT 1;
        """)

        if len(result) > 0:
            return result[0]['version']
        else:
            return 0
