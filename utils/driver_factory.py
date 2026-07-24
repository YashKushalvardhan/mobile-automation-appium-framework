# utils/driver_factory.py

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

class DriverFactory:
    @staticmethod
    def get_driver():
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "emulator-5554"

        # The APK path must be valid from the Appium SERVER's perspective,
        # not the test runner's. Since our Appium server runs on the
        # Windows host (not inside Docker), we need the Windows filesystem
        # path here, even when tests execute from inside a Linux container.
        default_apk_path = os.path.join(os.getcwd(), "apps", "ApiDemos.apk")
        options.app = os.environ.get("APK_PATH", default_apk_path)

        options.new_command_timeout = 300
        options.no_reset = False

        appium_server_url = os.environ.get(
            "APPIUM_SERVER_URL", "http://127.0.0.1:4723"
        )

        driver = webdriver.Remote(appium_server_url, options=options)
        return driver