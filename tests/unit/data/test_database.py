from mox.data import Database
from config import TestConfig
from tests.fixtures import database


def test_execute(database):
    database.execute('CREATE TABLE bad_cards (name text);')
    database.execute('INSERT INTO bad_cards (name) VALUES (\'Mox Amber\');')

    result = database.execute('SELECT * FROM bad_cards;')

    assert result == [{'name': 'Mox Amber'}]
