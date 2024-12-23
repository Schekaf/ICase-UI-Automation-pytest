from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage


def test_3_jobs(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    careers_page.scroll(careers_page.careers_locations_move_right)
    careers_page.click_see_all_jobs()
    quality_assurance = QualityAssurancePage(driver)
    quality_assurance.click_on_quality_assurance()
    quality_assurance.is_quality_assurance_page_open()
    quality_assurance.click_on_see_all_qa_jobs()
    quality_assurance.select_location("Istanbul, Turkey")
    quality_assurance.select_department("Quality Assurance")
    assert quality_assurance.is_job_list_present(), f"Job list is not present"


def test_4_jobs_quality_assurance(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    careers_page.scroll(careers_page.careers_locations_move_right)
    careers_page.click_see_all_jobs()
    quality_assurance = QualityAssurancePage(driver)
    quality_assurance.click_on_quality_assurance()
    quality_assurance.is_quality_assurance_page_open()
    quality_assurance.click_on_see_all_qa_jobs()
    quality_assurance.select_location("Istanbul, Turkey")
    quality_assurance.select_department("Quality Assurance")
    assert quality_assurance.check_all_job_criteria("Quality Assurance", "Quality Assurance", "Istanbul, Turkey")


def test_5_view_role(driver):
    home_page = HomePage(driver)
    home_page.wait_home_page_to_be_loaded()
    home_page.click_company()
    home_page.click_company_careers()
    careers_page = CareersPage(driver)
    careers_page.wait_careers_page_to_be_loaded()
    careers_page.scroll(careers_page.careers_locations_move_right)
    careers_page.click_see_all_jobs()
    quality_assurance = QualityAssurancePage(driver)
    quality_assurance.click_on_quality_assurance()
    quality_assurance.is_quality_assurance_page_open()
    quality_assurance.click_on_see_all_qa_jobs()
    quality_assurance.select_location("Istanbul, Turkey")
    quality_assurance.select_department("Quality Assurance")
    quality_assurance.click_on_view_role("Senior Software Quality Assurance Engineer", "Quality Assurance",
                                         "Istanbul, Turkey")
    assert quality_assurance.is_redirected_on_lever(), f"Couldn't get redirected to the Lever Application Page"

