# tests/test_browserstack_home_screen.py

from pages.home_page import HomePage


def test_app_list_item_visible_on_real_device(browserstack_driver):
    # Same test logic as our local test, but running on a real
    # Android device hosted on BrowserStack instead of a local emulator.
    home = HomePage(browserstack_driver)
    assert home.is_app_list_item_visible(), \
        "App list item not visible on home screen (BrowserStack real device)"