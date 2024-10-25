

from pages.home_page import HomePage


def test_open_home_page(driver):
    home_page = HomePage(driver)
    # Check Home Page Title
    actual_title = driver.title
    assert actual_title == home_page.title, f"Expected title to be '{home_page.title}' but got '{actual_title}'"
    # Check Home Page Logo
    home_page.wait_logo_to_be_loaded()
    logo_element = driver.find_element(*home_page.logo)
    assert logo_element.is_displayed(), f"Home page couldn't be loaded!"
