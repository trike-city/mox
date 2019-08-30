from mox.models import Player


def create_player(id=1, firstname='Joe', lastname='Noe'):
    return Player(id=id, firstname=firstname, lastname=lastname)


def test_equality_when_same():
    assert create_player() == create_player()


def test_equality_diff_ids():
    assert create_player(id=1) != create_player(id=2)


def test_equality_diff_firstname():
    assert create_player(firstname='Bob') != create_player(firstname='Mary')


def test_equality_diff_lastname():
    assert create_player(lastname='A') != create_player(lastname='B')
