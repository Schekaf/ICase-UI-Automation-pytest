from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.careers_page import CareersPage


def test_career_locations(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    actual_locations_list = careers_page.get_locations()
    expected_locations_list = careers_page.locations_list
    assert all(item in actual_locations_list for item in expected_locations_list), (
            f"Missing Locations found : " + str(list(set(expected_locations_list)-set(actual_locations_list))))
