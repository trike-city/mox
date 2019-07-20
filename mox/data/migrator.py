from .migration import Migration


class Migrator:
    def __init__(self, database, dir_path):
        self.database = database
        self.dir_path = dir_path

    def migrate_latest(self):
        migrations = self.__find_migrations()
        self.__perform_migrations(migrations)
        self.__create_schema_versions_table_if_needed()
        self.__store_new_version(migrations[-1])

    def __create_schema_versions_table_if_needed(self):
        self.database.execute('CREATE TABLE IF NOT EXISTS schema_versions (version INT);')

    def __find_migrations(self):
        file_paths = [f for f in self.dir_path.glob('**/*') if f.is_file()]
        migrations = [Migration(path) for path in file_paths]
        migrations.reverse()
        return migrations

    def __perform_migrations(self, migrations):
        for m in migrations:
            m.up(self.database)

    def __store_new_version(self, migration):
        sql = f'INSERT INTO schema_versions (version) VALUES ({migration.version});'
        self.database.execute(sql)
