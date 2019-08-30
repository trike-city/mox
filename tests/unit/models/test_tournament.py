from mox.models import Tournament


def create_tournament(id=1, name='TWC'):
    return Tournament(id=id, name=name)


def test_equality_when_same():
    assert create_tournament() == create_tournament()


def test_equality_diff_id():
    assert create_tournament(id=1) != create_tournament(id=2)


def test_equality_diff_name():
    assert create_tournament(name='Lobstercon') != create_tournament(name='TWC')
