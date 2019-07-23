from datetime import datetime


class Schema:
    def __init__(self, database):
        self.database = database
        self.__version = None

    def create_if_needed(self):
        self.__create_table_if_needed()
        self.__create_first_version_if_needed()

    def reset(self):
        self.database.execute(f'DROP TABLE IF EXISTS {self.__table_name};')

    @property
    def version(self):
        if self.__version is None:
            self.__load_version()
        return self.__version

    @version.setter
    def version(self, version):
        sql = f'INSERT INTO {self.__table_name} (version, created_at) VALUES (%s, %s);'
        self.database.execute(sql, (version, datetime.now()))
        self.__version = version

    def __create_table_if_needed(self):
        self.database.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.__table_name} (
            version INT,
            created_at TIMESTAMP NOT NULL
        );
        """)

    def __create_first_version_if_needed(self):
        result = self.database.execute(f'SELECT COUNT(*) FROM {self.__table_name};')
        if result[0]['count'] == 0:
            self.version = 0

    def __load_version(self):
        sql = f'SELECT (version) FROM {self.__table_name} ORDER BY created_at DESC LIMIT 1;'
        self.__version = self.database.execute(sql)[0]['version']

    @property
    def __table_name(self):
        return 'schema_versions'
