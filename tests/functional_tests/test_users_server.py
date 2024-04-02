import pytest
import time
from selenium import webdriver
from flask_testing import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from projet_11_oc.server import app



class Testfunctional(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app


    def setUp(self):
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()


    def test_login_with_valid_email(self):
        self.driver.get('http://localhost:5000/')
        time.sleep(3)
        email_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("john@simplylift.co")
        time.sleep(3)
        email_input.send_keys(Keys.RETURN)
        time.sleep(3)


    def test_reservation_and_purchase(self):
        self.driver.get('http://localhost:5000/book/Spring%20Festival/Simply%20Lift')
        time.sleep(3)
        places_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.NAME, "places"))
        )
        places_input.send_keys("2")
        time.sleep(3)
        places_input.send_keys(Keys.RETURN)
        time.sleep(3)







