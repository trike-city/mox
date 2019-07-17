import pytest

from mox.models import Tournament

def test_create():
    attributes = { 'name': 'Binomville', 'competitors': [] }
    tournament = Tournament.create(attributes)

    assert tournament.name == 'Binomville'
    assert len(tournament.competitors) == 0
