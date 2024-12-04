from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestUpdateTodo(BaseTest):
    def test_update_todo_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries']").click()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).clear()
        driver.find_element(AppiumBy.ID, Locators.TODO_TITLE_INPUT).send_keys("Buy groceries and fruits")
        driver.find_element(AppiumBy.ID, Locators.SUBMIT_TODO_BUTTON).click()

        # Verify update
        updated_todo_item = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']").text
        self.assertEqual(updated_todo_item, "Buy groceries and fruits")