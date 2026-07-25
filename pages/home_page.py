# pages/home_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    # Using ACCESSIBILITY_ID because resource-id ("android:id/text1") is
    # shared across all list items and is therefore not unique.
    APP_ITEM = (AppiumBy.ACCESSIBILITY_ID, "App")
    CONTENT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Content")
    GRAPHICS_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Graphics")
    VIEWS_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Views")

    def is_app_list_item_visible(self):
        return self.is_visible(*self.APP_ITEM)

    def click_app_item(self):
        self.click(*self.APP_ITEM)

    def click_content_item(self):
        self.click(*self.CONTENT_ITEM)

    def click_graphics_item(self):
        self.click(*self.GRAPHICS_ITEM)

    def click_views_item_with_scroll(self):
        # "Views" sits lower in the list and may not be visible without
        # scrolling, so we use the scroll-and-click helper instead of a
        # direct click.
        self.scroll_to_text_and_click("Views")

    def is_element_visible_by_text(self, text):
        # Generic helper for asserting any list item is visible by its
        # visible text/accessibility label.
        return self.is_visible(AppiumBy.ACCESSIBILITY_ID, text)