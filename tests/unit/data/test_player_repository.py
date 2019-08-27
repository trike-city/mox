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


def test_find_many(database):
    repo = PlayerRepository(database)
    p1 = repo.create({'firstname': 'Trike', 'lastname': 'Three'})
    p2 = repo.create({'firstname': 'Tetravus', 'lastname': 'Four'})
    p3 = repo.create({'firstname': 'Big', 'lastname': 'Daddy'})
    players = repo.find_many([p1.id, p2.id])

    assert players == [p1, p2]


def test_find_one(database):
    repo = PlayerRepository(database)
    player = repo.create(attributes)
    result = repo.find_one(player.id)

    assert result == player
