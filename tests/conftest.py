import pytest
from projet_11_oc.server import app


@pytest.fixture(scope='function')
def client():
    with app.test_client() as client:

        yield client


@pytest.fixture(scope='function')
def fixture_data():
    return {
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'numberOfPlaces': '25',
        'places': '2'
    }