from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDeleteTodo(BaseTest):
    def register_login_add_todo(self, email="newuser@gmail.com", password="password123", username="newuser"):
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
        
        # Add Todo
        driver.find_element(AppiumBy.ID, Locators.ADD_TODO_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).send_keys("Buy groceries")
        driver.find_element(AppiumBy.ID, Locators.TODO_DESC_INPUT).send_keys("Milk, eggs, bread")
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()

        todo_item = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']").text
        self.assertEqual(todo_item, "Buy groceries")

    def test_delete_todo_successful(self):
        driver = self.driver
        self.register_login_add_todo()

        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']").click()
        driver.find_element(AppiumBy.ID, Locators.DELETE_TODO_BUTTON).click()

        # Verify the Todo is deleted
        todo_list = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']")
        self.assertEqual(len(todo_list), 0)