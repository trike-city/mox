from mox.data import PlayerRepository
from tests.fixtures import database


attributes = {'firstname': 'Richard', 'lastname': 'Garfield'}


def test_create_returns_player(database):
    repo = PlayerRepository(database)
    player = repo.create(attributes)

    assert player.id is not None
    assert player.firstname == 'Richard'
    assert player.lastname == 'Garfield'


def test_create_persist_player(database):
    repo = PlayerRepository(database)
    repo.create(attributes)
    result = database.execute('SELECT * FROM players;')[0]

    assert result['firstname'] == 'Richard'
    assert result['lastname'] == 'Garfield'
