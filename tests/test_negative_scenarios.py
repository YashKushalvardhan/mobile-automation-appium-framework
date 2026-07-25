# tests/test_negative_scenarios.py

import pytest
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from pages.home_page import HomePage


def test_nonexistent_element_raises_timeout(driver):
    # This test intentionally looks for an element that does not exist
    # on the home screen, to confirm our framework fails predictably
    # (raises TimeoutException) rather than hanging indefinitely or
    # crashing with an unrelated error.
    home = HomePage(driver)

    with pytest.raises(TimeoutException):
        home.find_element(AppiumBy.ACCESSIBILITY_ID, "ThisElementDoesNotExist123")