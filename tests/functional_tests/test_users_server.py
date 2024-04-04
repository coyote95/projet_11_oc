"""
This module contains functional tests using Selenium to verify the behavior
of the GUDLFT web application.

Functions:
    - create_app(self): Configuration method to create an instance of the Flask application for testing.
    - setUp(self): Configuration method executed before each test to initialize the Selenium web browser.
    - tearDown(self): Method executed after each test to close the Selenium web browser.
    - test_login_with_valid_email(self): Tests the login functionality with a valid email address.
    - test_reservation_and_purchase(self): Tests the reservation and purchase process for an event.

Preconditions:
    - The Flask development server must be running locally on port 5000.
    - The GUDLFT web application must be accessible at URL http://localhost:5000/.

Note:
    Make sure the Chrome browser is installed on your system and the path to the Chrome WebDriver
    driver is correctly configured, or use a driver manager like webdriver_manager to automatically
    handle downloading and installing the driver.

Usage Example:
    pytest test_functional.py
"""

import pytest
import time
from flask_testing import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from server import app


class Testfunctional(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_valid_email(self):
        self.driver.get("http://localhost:5000/")
        time.sleep(3)
        email_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("john@simplylift.co")
        time.sleep(3)
        email_input.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_reservation_and_purchase(self):
        self.driver.get("http://localhost:5000/book/Spring%20Festival/Simply%20Lift")
        time.sleep(3)
        places_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.NAME, "places"))
        )
        places_input.send_keys("2")
        time.sleep(3)
        places_input.send_keys(Keys.RETURN)
        time.sleep(3)
