# utils/driver_factory.py

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

class DriverFactory:
    @staticmethod
    def get_driver():
        # Path to APK (relative to project root)
        apk_path = os.path.join(os.getcwd(), "apps", "ApiDemos.apk")

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "emulator-5554"   # adb devices name
        options.app = apk_path
        options.new_command_timeout = 300
        options.no_reset = False   # for every state freshapp

        # Appium 2.x default server URL (no /wd/hub needed)
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return driver