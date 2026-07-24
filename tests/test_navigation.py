# tests/test_navigation.py

from pages.home_page import HomePage


def test_navigate_to_app_screen_and_back(driver):
    home = HomePage(driver)

    # Step 1: Confirm we're starting from the home screen
    assert home.is_app_list_item_visible(), "App item not found on home screen"

    # Step 2: Tap on "App" to navigate into that section
    home.click_app_item()

    # Step 3: Confirm navigation happened by checking a home-screen-only
    # element ("Content") is no longer visible
    assert home.wait_until_invisible(*home.CONTENT_ITEM), \
        "Did not navigate away from home screen"

    # Step 4: Go back using Android's back navigation
    driver.back()

    # Step 5: Confirm we're back on the home screen
    assert home.is_app_list_item_visible(), \
        "Did not return to home screen after pressing back"


def test_navigate_to_content_screen_and_back(driver):
    home = HomePage(driver)

    assert home.is_app_list_item_visible(), "App item not found on home screen"

    home.click_content_item()

    # Same pattern — confirm a different home-only element disappeared
    assert home.wait_until_invisible(*home.APP_ITEM), \
        "Did not navigate away from home screen"

    driver.back()

    assert home.is_app_list_item_visible(), \
        "Did not return to home screen after pressing back"