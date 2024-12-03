from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestAddTodo(BaseTest):
    def test_add_todo_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.ID, Locators.ADD_TODO_BUTTON).click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).send_keys("Buy groceries")
        driver.find_element(AppiumBy.ID, Locators.TODO_DESC_INPUT).send_keys("Milk, eggs, bread")
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()

        # Verify todo added
        todo_item = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']").text
        self.assertEqual(todo_item, "Buy groceries")
