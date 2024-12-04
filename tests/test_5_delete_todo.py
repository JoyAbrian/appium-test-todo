from utils.base_test import BaseTest
from utils.locators import Locators
from appium.webdriver.common.appiumby import AppiumBy

class TestDeleteTodo(BaseTest):
    def test_delete_todo_successful(self):
        driver = self.driver
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']").click()
        driver.find_element(AppiumBy.ID, Locators.DELETE_TODO_BUTTON).click()

        # Verify deletion
        todo_list = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy groceries and fruits']")
        self.assertEqual(len(todo_list), 0)