from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(BaseTest):
    def create_account(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.USERNAME_INPUT).send_keys("newuser")
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.REGISTER_BUTTON).click()

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.ID, Locators.LOGIN_BUTTON))
            )
        except:
            self.fail("Failed to navigate to login page after registration.")

    def test_login_1_invalid_credential(self):
        driver = self.driver

        self.create_account()
        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("wrongemail@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("wrongpassword")
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

        # Verify invalid credentials toast message
        toast_message_xpath = "//*[contains(@text, 'Invalid email or password')]"
        try:
            toast_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
            )
            self.assertEqual(toast_element.text, "Invalid email or password")
        except:
            self.fail("Toast message 'Invalid email or password' not found.")
    
    def test_login_2_invalid_password(self):
        driver = self.driver

        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("wrongpassword")
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

        # Verify invalid credentials toast message
        toast_message_xpath = "//*[contains(@text, 'Invalid email or password')]"
        try:
            toast_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
            )
            self.assertEqual(toast_element.text, "Invalid email or password")
        except:
            self.fail("Toast message 'Invalid email or password' not found.")
    
    def test_login_3_successful(self):
        driver = self.driver

        driver.find_element(AppiumBy.ID, Locators.EMAIL_INPUT).send_keys("newuser@gmail.com")
        driver.find_element(AppiumBy.ID, Locators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(AppiumBy.ID, Locators.LOGIN_BUTTON).click()

        # Verify the transition to MainActivity
        try:
            WebDriverWait(driver, 5).until(
                lambda d: d.current_activity == ".MainActivity"
            )
            self.assertEqual(driver.current_activity, ".MainActivity")
        except:
            self.fail("Failed to transition to MainActivity.")

