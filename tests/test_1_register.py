from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestRegister(BaseTest):
    def test_register_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys("newuser")
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

    def test_register_duplicate(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys("newuser")
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

        # Verify duplicate error message
        error_message = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='User already exists']").text
        self.assertEqual(error_message, "User already exists")