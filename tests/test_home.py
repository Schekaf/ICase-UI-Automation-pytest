from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


def test_open_home_page(driver):
    home_page = HomePage(driver)

    actual_title = driver.title
    assert actual_title == home_page.title, f"Expected title to be '{home_page.title}' but got '{actual_title}'"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_page.logo))
    logo_element = driver.find_element(*home_page.logo)
    assert logo_element.is_displayed(), f"Home page couldn't be loaded!"
