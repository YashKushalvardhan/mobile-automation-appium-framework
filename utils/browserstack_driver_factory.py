# utils/browserstack_driver_factory.py

from appium import webdriver
from appium.options.common.base import AppiumOptions
import os


class BrowserStackDriverFactory:
    @staticmethod
    def get_driver():
        username = os.environ.get("BROWSERSTACK_USERNAME")
        access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")

        if not username or not access_key:
            raise EnvironmentError(
                "BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY "
                "must be set as environment variables."
            )

        # The app_url is generated once by uploading the APK to
        # BrowserStack (see the curl upload command). This points
        # BrowserStack to the already-hosted app on their servers.
        app_url = os.environ.get("BROWSERSTACK_APP_URL")

        options = AppiumOptions()
        options.set_capability("platformName", "Android")
        options.set_capability("appium:app", app_url)

        # bstack:options groups BrowserStack-specific configuration,
        # separate from standard Appium/W3C capabilities.
        options.set_capability("bstack:options", {
            "userName": username,
            "accessKey": access_key,
            "deviceName": "Google Pixel 7",
            "osVersion": "13.0",
            "projectName": "Mobile Automation Appium Framework",
            "buildName": "BrowserStack Real Device Run",
            "sessionName": "ApiDemos Home Screen Test",
        })

        # BrowserStack's remote Appium hub URL — this replaces our local
        # http://127.0.0.1:4723, since the session now runs on
        # BrowserStack's infrastructure instead of our local Appium server.
        remote_url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

        driver = webdriver.Remote(remote_url, options=options)
        return driver