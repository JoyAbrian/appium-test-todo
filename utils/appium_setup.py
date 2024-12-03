from appium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
def get_driver():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": os.getenv("PLATFORM_VERSION"),
        "deviceName": os.getenv("DEVICE_NAME"),
        "app": "app/app-debug.apk",
        "automationName": "UiAutomator2"
    }
    appium_server = os.getenv("APPIUM_SERVER")
    implicit_wait = 10
    
    driver = webdriver.Remote(appium_server, desired_capabilities)
    driver.implicitly_wait(implicit_wait)
    return driver