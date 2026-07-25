# pages/base_page.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        el = self.find_element(by, value)
        el.click()

    def is_visible(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except TimeoutException:
            return False

    def wait_until_invisible(self, by, value):
        return self.wait.until(EC.invisibility_of_element_located((by, value)))

    def scroll_to_text_and_click(self, text):
        # Uses Android's native UiScrollable mechanism to scroll a
        # scrollable list until the given text is visible, then clicks it.
        # This is more reliable than manual swipe coordinates because it
        # relies on Android's own accessibility scrolling logic.
        scroll_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )
        element = self.find_element(*scroll_locator)
        element.click()