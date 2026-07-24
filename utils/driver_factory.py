# utils/driver_factory.py

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

class DriverFactory:
    @staticmethod
    def get_driver():
        apk_path = os.path.join(os.getcwd(), "apps", "ApiDemos.apk")

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "emulator-5554"
        options.app = apk_path
        options.new_command_timeout = 300
        options.no_reset = False

        # Read Appium server URL from an environment variable.
        # Defaults to localhost for when tests run directly on the host machine.
        # When running inside Docker, this will be overridden to point
        # to the host machine's Appium server via host.docker.internal.
        appium_server_url = os.environ.get(
            "APPIUM_SERVER_URL", "http://127.0.0.1:4723"
        )

        driver = webdriver.Remote(appium_server_url, options=options)
        return driver