# tests/test_scroll.py

from pages.home_page import HomePage


def test_scroll_to_views_and_open(driver):
    home = HomePage(driver)

    # Confirm we start on the home screen
    assert home.is_app_list_item_visible(), "App item not found on home screen"

    # Scroll down the list and tap "Views" — this exercises Android's
    # native scrollable list gesture handling
    home.click_views_item_with_scroll()

    # Confirm navigation happened by checking a home-only element
    # is no longer visible
    assert home.wait_until_invisible(*home.APP_ITEM), \
        "Did not navigate away from home screen after scrolling to Views"

    driver.back()

    assert home.is_app_list_item_visible(), \
        "Did not return to home screen after pressing back"