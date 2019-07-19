import pytest

from mox.data import Database
from config import TestConfig


def test_execute():
    db = Database(TestConfig())

    db.open()
    db.execute('CREATE TABLE bad_cards (name text);')
    db.execute('INSERT INTO bad_cards (name) VALUES (\'Mox Amber\');')

    result = db.execute('SELECT * FROM bad_cards;')

    db.execute('DROP TABLE bad_cards;')
    db.close()

    assert result == [{'name': 'Mox Amber'}]
