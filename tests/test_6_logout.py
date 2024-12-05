from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout(BaseTest):
    def register_and_login(self, email="newuser@gmail.com", password="password123", username="newuser"):
        driver = self.driver

        # Registration process
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys(username)
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

        # Verify navigation to login page after registration
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.ID, Locators.LOGIN_BUTTON))
            )
        except:
            self.fail("Failed to navigate to login page after registration.")

        # Login process
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

        # Verify transition to MainActivity
        try:
            WebDriverWait(driver, 5).until(
                lambda d: d.current_activity == ".MainActivity"
            )
            self.assertEqual(driver.current_activity, ".MainActivity")
        except:
            self.fail("Failed to transition to MainActivity.")

    def test_logout_successful(self):
        driver = self.driver
        self.register_and_login()

        driver.find_element(AppiumBy.ID, Locators.PROFILE_TOGGLE).click()
        driver.find_element(AppiumBy.ID, Locators.LOGOUT_BUTTON).click()

        try:
            login_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.ID, Locators.LOGIN_BUTTON))
            )
            self.assertTrue(login_button.is_displayed(), "Login button is not displayed after logout")
        except Exception:
            self.fail("Failed to redirect to the login screen after logout")