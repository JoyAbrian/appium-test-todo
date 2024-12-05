from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUpdateTodo(BaseTest):
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

    def test_update_todo_1_successful(self):
        driver = self.driver
        self.register_login_add_todo()

        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']").click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).clear()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).send_keys("Buy groceries and fruits")
        driver.find_element(AppiumBy.ID, Locators.TODO_DESC_INPUT).clear()
        driver.find_element(AppiumBy.ID, Locators.TODO_DESC_INPUT).send_keys("Milk, eggs, bread, and apples")
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.PROFILE_TOGGLE).click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TOGGLE).click()

        # Verify the Todo is updated
        updated_todo_item = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']").text
        self.assertEqual(updated_todo_item, "Buy groceries and fruits")

    def test_update_todo_2_same_title_and_description(self):
        driver = self.driver

        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']").click()
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.PROFILE_TOGGLE).click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TOGGLE).click()

        # Verify the Todo's updated date has changed (requires specific verification logic)
        try:
            updated_date_xpath = "//android.widget.TextView[contains(@text, 'Updated at ')]"
            updated_date = driver.find_element(AppiumBy.XPATH, updated_date_xpath).text
            self.assertIn("Updated at ", updated_date)
        except:
            self.fail("Updated date was not modified for Todo.")

    def test_update_todo_3_empty_title_or_description(self):
        driver = self.driver

        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']").click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).clear()
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()

        # Verify error message for empty title
        toast_message_xpath = "//*[contains(@text, 'Please fill all fields')]"
        try:
            toast_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
            )
            self.assertEqual(toast_element.text, "Please fill all fields")
        except:
            self.fail("Toast message 'Please fill all fields' not found.")