"""
Unit tests for the showSummary functionality in the GUDLFT web application.

This module contains two test cases to verify the behavior of the showSummary endpoint in the GUDLFT application.
The tests import the 'client' fixture from the conftest module to simulate requests with different email inputs.

test_show_summary_valid_email:
    Test case to check the response when providing a valid email address.

test_show_summary_invalid_email:
    Test case to check the response when providing an invalid email address.
"""

from projet_11_oc.tests.conftest import client


def test_show_summary_valid_email(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_show_summary_invalid_email(client):
    response = client.post("/showSummary", data={"email": "invalid@example.com"})
    assert response.status_code == 200
    assert b"Sorry, that email wasn&#39;t found." in response.data
