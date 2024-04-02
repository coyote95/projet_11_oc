import pytest
from projet_11_oc.server import app


@pytest.fixture
def client():
    with app.test_client() as client:

        yield client


@pytest.fixture
def fixture_data():
    return {"competition": "Spring Festival", "club": "Simply Lift", "places": "6"}


@pytest.fixture
def wrong_fixture_data():
    return {"competition": "Spring Festival", "club": "Simply Lift", "places": "13"}
