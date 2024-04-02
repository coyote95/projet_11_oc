"""
Unit tests for loading clubs and competitions data in the GUDLFT server module.
"""

import pytest
from projet_11_oc.server import loadClubs, loadCompetitions


def test_loadClubs():
    clubs = loadClubs()
    assert isinstance(clubs, list)
    assert len(clubs) > 0
    for club in clubs:
        assert "name" in club
        assert "email" in club
        assert "points" in club


def test_loadCompetitions():
    competitions = loadCompetitions()
    assert isinstance(competitions, list)
    assert len(competitions) > 0
    for competition in competitions:
        assert "name" in competition
        assert "date" in competition
        assert "numberOfPlaces" in competition
