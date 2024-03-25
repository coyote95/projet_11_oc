from projet_11_oc.tests.conftest import client, fixture_data


# def test_purchase_places_status_code(client, fixture_data):
#
#         response = client.post('/purchasePlaces', data=fixture_data)
#         assert response.status_code == 200
#
# def test_purchase_places_update_places(client, fixture_data):
#     print(fixture_data)
#     response = client.post('/purchasePlaces', data=fixture_data)
#     assert fixture_data['numberOfPlaces'] is not None
#
#     initial_places = int(fixture_data['numberOfPlaces'])
#     places_to_purchase = int(fixture_data['places'])
#
#     updated_places = initial_places - places_to_purchase
#     print(updated_places)
#
#     # assert b'Number of Places: 23'in response.data
#     print (response.data)
#
#     assert b'Great-booking complete!' in response.data

def test_purchase_places(client):
    form_data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '2',
        'numberOfPlaces':'25'

    }

    response = client.post('/purchasePlaces', data=form_data)
    assert response.status_code == 200

    initial_places = int(form_data['numberOfPlaces'])
    places_to_purchase = int(form_data['places'])
    updated_places = initial_places - places_to_purchase

    print(response.data)
    assert b'Number of Places: 23'in response.data
    assert b'Great-booking complete!' in response.data
