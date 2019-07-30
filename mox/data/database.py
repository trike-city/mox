import psycopg2
import psycopg2.extras


class Database:
    def __init__(self, config):
        self.host = config.PG_HOST
        self.port = config.PG_PORT
        self.name = config.DATABASE
        self.user = config.PG_USER
        self.password = config.PG_PASSWORD

    def open(self):
        url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
        self.connection = psycopg2.connect(url)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def close(self):
        if not hasattr(self, 'connection'):
            raise ValueError('No connection to close. Did you run open()?')
        else:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def execute(self, sql):
        if not hasattr(self, 'connection'):
            raise ValueError('No connection available. Did you run open()?')
        else:
            self.cursor.execute(sql)

            if self.__records_are_available:
                return self.cursor.fetchall()
            else:
                return True

    def rollback(self):
        if not hasattr(self, 'connection'):
            raise ValueError('No connection available. Did you run open()?')
        else:
            self.connection.rollback()

    @property
    def __records_are_available(self):
        return self.cursor.description is not None
