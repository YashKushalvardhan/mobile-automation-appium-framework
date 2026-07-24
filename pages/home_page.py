# pages/home_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    # Using ACCESSIBILITY_ID (content-desc) because resource-id is shared
    # across all list items ("android:id/text1"), making it non-unique.
    # content-desc matches the visible text and is unique per item.
    APP_ITEM = (AppiumBy.ACCESSIBILITY_ID, "App")
    CONTENT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Content")
    GRAPHICS_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Graphics")

    def is_app_list_item_visible(self):
        return self.is_visible(*self.APP_ITEM)

    def click_app_item(self):
        self.click(*self.APP_ITEM)

    def click_content_item(self):
        self.click(*self.CONTENT_ITEM)

    def click_graphics_item(self):
        self.click(*self.GRAPHICS_ITEM)