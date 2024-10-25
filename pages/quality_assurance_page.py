from selenium.webdriver.common.by import By

from utils.common import Common


class QualityAssurancePage(Common):
    # Locators
    careers_jobs_quality_assurance = (By.XPATH, "//*[contains(@class, 'job-title')]//h3[text()='Quality Assurance']")
    careers_jobs_quality_assurance_big_title = (
    By.XPATH, "//*[contains(@class, 'big-title')]//h3[text()='Quality Assurance']")
    see_all_qa_jobs_button = (By.XPATH, "//*[contains(@class, 'btn btn') and text()='See all QA jobs']")
    filter_by_department = (By.ID, 'select2-filter-by-department-container')

    def click_on_quality_assurance(self):
        self.driver.find_element(*self.careers_jobs_quality_assurance).click()

    def is_quality_assurance_page_open(self) -> bool:
        return self.is_open(self.careers_jobs_quality_assurance_big_title)

    def click_on_see_all_qa_jobs(self):
        self.driver.find_element(*self.see_all_qa_jobs_button).click()

    def select_department(self, department: str):
        self.driver.find_element(*self.filter_by_department).click()
        dynamic_locator = (By.XPATH, f"//*[contains(@id, 'select2-filter-by-department-result-') and contains(@id, '{department}')]")
        self.driver.find_element(*dynamic_locator).click()

    def is_filtered_by_department(self, department: str) -> bool:
        element = self.driver.find_element(*self.filter_by_department)
        return element.text == department
