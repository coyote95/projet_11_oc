"""
Unit test function verifies the behavior of the booking process in the GUDLFT application.
It imports the 'client' fixture from the conftest module to simulate requests to the application. The test checks:
- If the booking page is successfully loaded (status code 200).
- If the page contains the expected information about booking for the Spring Festival event.
"""

from ..conftest import client


def test_valid_booking(client):
    response = client.get("/book/Spring%20Festival/Simply%20Lift")
    assert response.status_code == 200
    assert b"Booking for" in response.data
    assert b"Spring Festival" in response.data
