"""
Unit tests for purchasing places functionality in the GUDLFT web application.

This module contains several test cases to verify the behavior of the purchasePlaces endpoint in the GUDLFT application.
The tests import the 'client' and 'fixture_data' fixtures from the conftest module to simulate requests and data required for testing.

test_purchase_places_status_code:
    Test case to check the status code of the purchasePlaces endpoint.

test_purchase_places_points_allowed:
    Test case to verify the purchase of places when the club has sufficient points.

test_purchase_places_points_unallowed:
    Test case to verify the purchase of places when the club has insufficient points.

test_purchase_places_more_twelve_points:
    Test case to verify the purchase of places when the club tries to book more than 12 places.

test_purchase_places_past_competition:
    Test case to verify the purchase of places for a past competition.

test_purchase_places_update_points:
    Test case to verify the update of points after purchasing places.
"""

from ..conftest import client, fixture_data
from server import competitions, clubs  # Import the global variables


def test_purchase_places_status_code(client, fixture_data):

    response = client.post("/purchasePlaces", data=fixture_data)
    assert response.status_code == 200


def test_purchase_places_points_allowed(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]
    mocked_competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 70, "date": "2025-03-27 10:00:00"}
    ]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr("server.clubs", mocked_clubs)
    monkeypatch.setattr("server.competitions", mocked_competitions)

    response = client.post("/purchasePlaces", data=fixture_data)

    print(response.data)
    assert b"Number of Places: 64" in response.data  # 70 - 6 places
    assert b"Great-booking complete!" in response.data


def test_purchase_places_points_unallowed(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 2}]  # 6 places in the fixture
    mocked_competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 70, "date": "2025-03-27 10:00:00"}
    ]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr("server.clubs", mocked_clubs)
    monkeypatch.setattr("server.competitions", mocked_competitions)

    response = client.post("/purchasePlaces", data=fixture_data)

    print(response.data)
    assert (
        b"Error: Insufficient places available for booking!" in response.data
    )  # 6places in the fixture


def test_purchase_places_more_twelve_points(client, wrong_fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]  # 6 places in the fixture
    mocked_competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 70, "date": "2025-03-27 10:00:00"}
    ]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr("server.clubs", mocked_clubs)
    monkeypatch.setattr("server.competitions", mocked_competitions)

    response = client.post("/purchasePlaces", data=wrong_fixture_data)

    print(response.data)
    assert b"Error: You cannot book more than 12 places!" in response.data


def test_purchase_places_past_competition(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]  # 6 places in the fixture
    mocked_competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 70, "date": "2020-03-27 10:00:00"}
    ]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr("server.clubs", mocked_clubs)
    monkeypatch.setattr("server.competitions", mocked_competitions)

    response = client.post("/purchasePlaces", data=fixture_data)

    print(response.data)
    assert b"Error: The competition has already passed." in response.data


def test_purchase_places_update_points(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]  # 6 places in the fixture
    mocked_competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 70, "date": "2025-03-27 10:00:00"}
    ]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr("server.clubs", mocked_clubs)
    monkeypatch.setattr("server.competitions", mocked_competitions)

    response = client.post("/purchasePlaces", data=fixture_data)

    print(response.data)
    assert b"Points available: 4" in response.data  # 10 points - 6 places
