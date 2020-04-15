from appium import webdriver as AppiumDriver
from selenium import webdriver as ChromeDriver
import pytest
import os

class Test():
    def test_open_two_sessions(self):
            # Appium
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
        }
        desired_caps['app'] = os.path.join(
            os.path.dirname(__file__),
            'app/ApiDemos-debug.apk')

        path = "driver/chromedriver"
        chrome_driver = ChromeDriver.Chrome(executable_path=path)

        chrome_driver.get('http://www.google.com')
        
        appium_driver = AppiumDriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
        appium_driver.quit()
        chrome_driver.quit()

