import time
import pytest

from pages.home_page import HomePage
from pages.careers_page import CareersPage
@pytest.mark.skip
def test_2_1_teams(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    careers_page.scroll(careers_page.careers_locations_move_right)
    careers_page.click_see_all_jobs()
    actual_teams_list = careers_page.get_teams_title_list()
    expected_teams_list = careers_page.jobs_list
    assert all(item in actual_teams_list for item in expected_teams_list), (
            f"Missing Teams found : " + str(list(set(expected_teams_list) - set(actual_teams_list))))
    assert careers_page.is_team_blocks_open()


def test_2_2_life_at_insider(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    careers_page.scroll(careers_page.careers_life_at_Insider)
    assert careers_page.is_life_at_insider_block_open(), f"Is Life at Insider blocks are not open"
