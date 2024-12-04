from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
import os

load_dotenv()
def get_driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", os.getenv("PLATFORM_VERSION"))
    options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
    options.set_capability("appPackage", "com.ruukaze.simple_todo_app")
    options.set_capability("appActivity", "com.ruukaze.simple_todo_app.MainActivity")

    appium_server = os.getenv("APPIUM_SERVER")
    implicit_wait = 10
    driver = webdriver.Remote(appium_server, options=options)
    driver.implicitly_wait(implicit_wait)
    return driver
