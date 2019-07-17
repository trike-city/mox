import pytest

from mox.models import Player


def test_create():
    attributes = { 'firstname': 'Binom', 'lastname': 'Missieu' }
    player = Player.create(attributes)

    assert player.firstname == 'Binom'
    assert player.lastname == 'Missieu'
