from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestLogin(BaseTest):
    def test_login_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

    def test_login_invalid_password(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("wrongpassword")
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

        # Verify invalid password message
        error_message = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Invalid credentials']").text
        self.assertEqual(error_message, "Invalid credentials")