import unittest
from utils.appium_setup import get_driver

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()