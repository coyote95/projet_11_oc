from projet_11_oc.tests.conftest import client, fixture_data
from projet_11_oc.server import competitions, clubs  # Import the global variables



def test_purchase_places_status_code(client, fixture_data):

        response = client.post('/purchasePlaces', data=fixture_data)
        assert response.status_code == 200


def test_purchase_places_points_allowed(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]
    mocked_competitions = [{"name": "Spring Festival", "numberOfPlaces": 70,"date":"2025-03-27 10:00:00"}]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr('projet_11_oc.server.clubs', mocked_clubs)
    monkeypatch.setattr('projet_11_oc.server.competitions', mocked_competitions)

    response = client.post('/purchasePlaces', data=fixture_data)

    print (response.data)
    assert b'Number of Places: 64'in response.data #70 - 6 places
    assert b'Great-booking complete!' in response.data


def test_purchase_places_points_unallowed(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 2}]   # 6 places in the fixture
    mocked_competitions = [{"name": "Spring Festival", "numberOfPlaces": 70,"date":"2025-03-27 10:00:00"}]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr('projet_11_oc.server.clubs', mocked_clubs)
    monkeypatch.setattr('projet_11_oc.server.competitions', mocked_competitions)

    response = client.post('/purchasePlaces', data=fixture_data)

    print (response.data)
    assert b'Error: Insufficient places available for booking!'in response.data #6places in the fixture

def test_purchase_places_more_twelve_points(client, wrong_fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 2}]   # 6 places in the fixture
    mocked_competitions = [{"name": "Spring Festival", "numberOfPlaces": 70,"date":"2025-03-27 10:00:00"}]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr('projet_11_oc.server.clubs', mocked_clubs)
    monkeypatch.setattr('projet_11_oc.server.competitions', mocked_competitions)

    response = client.post('/purchasePlaces', data=wrong_fixture_data)

    print (response.data)
    assert b'Error: You cannot book more than 12 places!'in response.data

def test_purchase_places_past_competition(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 2}]   # 6 places in the fixture
    mocked_competitions = [{"name": "Spring Festival", "numberOfPlaces": 70,"date":"2020-03-27 10:00:00"}]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr('projet_11_oc.server.clubs', mocked_clubs)
    monkeypatch.setattr('projet_11_oc.server.competitions', mocked_competitions)

    response = client.post('/purchasePlaces', data=fixture_data)

    print (response.data)
    assert b'Error: The competition has already passed.'in response.data

