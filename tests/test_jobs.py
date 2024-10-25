from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage


def test_jobs(driver):
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
    quality_assurance.is_filtered_by_department("Quality Assurance")



