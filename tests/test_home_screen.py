# tests/test_home_screen.py

from pages.home_page import HomePage

def test_app_list_item_visible(driver):
    home = HomePage(driver)
    assert home.is_app_list_item_visible(), "App list item not visible on home screen"