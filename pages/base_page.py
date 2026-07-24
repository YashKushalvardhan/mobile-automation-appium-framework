# pages/base_page.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Explicit wait instead of time.sleep()

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        el = self.find_element(by, value)
        el.click()

    def is_visible(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except Exception:
            return False

    def wait_until_invisible(self, by, value):
        # Used to confirm navigation away from a screen
        # Returns True once the element is no longer present/visible
        return self.wait.until(EC.invisibility_of_element_located((by, value)))