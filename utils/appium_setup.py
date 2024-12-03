from appium import webdriver

def get_driver():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "emulator-5554",
        "app": "app/app-debug.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(10)
    return driver