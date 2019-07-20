from .migration import Migration


class Migrator:
    def __init__(self, database, dir_path):
        self.database = database
        self.dir_path = dir_path

    def migrate_latest(self):
        for migration in self.__find_migrations():
            migration.up(self.database)

    def __find_migrations(self):
        file_paths = [f for f in self.dir_path.glob('**/*') if f.is_file()]
        migrations = [Migration(path) for path in file_paths]
        migrations.reverse()
        return migrations
