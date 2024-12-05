from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegister(BaseTest):
    def test_register_1_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys("newuser")
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

        # Verify success toast message
        toast_message_xpath = "//*[contains(@text, 'Registration successful')]"
        try:
            toast_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
            )
            self.assertEqual(toast_element.text, "Registration successful")
        except:
            self.fail("Toast message 'Registration successful' not found.")

    def test_register_2_duplicate(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys("newuser")
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

        # Verify duplicate user toast message
        toast_message_xpath = "//*[contains(@text, 'User already exists')]"
        try:
            toast_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
            )
            self.assertEqual(toast_element.text, "User already exists")
        except:
            self.fail("Toast message 'User already exists' not found.")