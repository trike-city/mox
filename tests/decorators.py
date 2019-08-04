from mox.data import Schema


def with_clean_schema_version(func):
    def wrapper(database):
        Schema(database).reset()
        func(database)

    return wrapper
