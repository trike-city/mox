from mox.models import Participation


def test_build():
    attributes = {'id': 1, 'tournament_id': 2, 'player_id': 3}
    subject = Participation.build(attributes)

    assert subject.id == 1
    assert subject.tournament_id == 2
    assert subject.player_id == 3
