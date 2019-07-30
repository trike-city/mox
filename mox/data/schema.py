from datetime import datetime


class Schema:
    def __init__(self, database):
        self.database = database
        self.__version = None

    def create_if_needed(self):
        self.__create_table_if_needed()
        self.__create_first_version_if_needed()

    @property
    def version(self):
        if self.__version is None:
            self.__load_version()
        return self.__version

    @version.setter
    def version(self, version):
        sql = 'INSERT INTO schema_versions (version, created_at) VALUES (%s, %s);'
        self.database.execute(sql, (version, datetime.now()))
        self.__version = version

    def __create_table_if_needed(self):
        self.database.execute("""
        CREATE TABLE IF NOT EXISTS schema_versions (
            version INT,
            created_at TIMESTAMP NOT NULL
        );
        """)

    def __create_first_version_if_needed(self):
        result = self.database.execute('SELECT COUNT(*) FROM schema_versions;')
        if result[0]['count'] == 0:
            self.version = 0

    def __load_version(self):
        sql = 'SELECT (version) FROM schema_versions ORDER BY created_at DESC LIMIT 1;'
        self.__version = self.database.execute(sql)[0]['version']
