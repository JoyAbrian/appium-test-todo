from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestLogout(BaseTest):
    def test_logout_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.PROFILE_TOGGLE).click()
        driver.find_element(AppiumBy.ID, Locators.LOGOUT_BUTTON).click()

        # Verify redirect to login screen
        login_button = driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON)
        self.assertTrue(login_button.is_displayed())