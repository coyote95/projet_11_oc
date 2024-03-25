from projet_11_oc.tests.conftest import client, fixture_data
from projet_11_oc.server import competitions, clubs  # Import the global variables



def test_purchase_places_status_code(client, fixture_data):

        response = client.post('/purchasePlaces', data=fixture_data)
        assert response.status_code == 200

def test_purchase_places_points_allowed(client, fixture_data, monkeypatch):
    print(fixture_data)

    # Set the desired values for the global variables
    mocked_clubs = [{"name": "Simply Lift", "points": 10}]
    mocked_competitions = [{"name": "Spring Festival", "numberOfPlaces": 70}]

    # Use monkeypatch to substitute the global variables
    monkeypatch.setattr('projet_11_oc.server.clubs', mocked_clubs)
    monkeypatch.setattr('projet_11_oc.server.competitions', mocked_competitions)

    response = client.post('/purchasePlaces', data=fixture_data)

    print (response.data)
    assert b'Number of Places: 64'in response.data #70 - 6 places
    assert b'Great-booking complete!' in response.data


