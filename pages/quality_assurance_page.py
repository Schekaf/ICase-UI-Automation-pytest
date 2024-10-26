from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.common import Common


class QualityAssurancePage(Common):
    # Locators
    careers_jobs_quality_assurance = (By.XPATH, "//*[contains(@class, 'job-title')]//h3[text()='Quality Assurance']")
    careers_jobs_quality_assurance_big_title = (
    By.XPATH, "//*[contains(@class, 'big-title')]//h3[text()='Quality Assurance']")
    careers_jobs_product_design = (By.XPATH, "//*[contains(@class, 'job-title')]//h3[text()='Product Design']")
    see_all_qa_jobs_button = (By.XPATH, "//*[contains(@class, 'btn btn') and text()='See all QA jobs']")
    filter_by_department = (By.ID, 'select2-filter-by-department-container')
    filter_by_department_list = (By.ID, "select2-filter-by-department-results")
    location = (By.XPATH, "//*[@id='select2-filter-by-location-container']")
    location_list = (By.XPATH, "//ul[contains(@class, 'select2-results__options')]")
    job_list = (By.ID, "jobs-list")
    job_list_items = (By.XPATH, "//div[@id='jobs-list']/div[contains(@class, 'position-list-item')]")
    bottom_pagination = (By.ID, 'pagination')

    def click_on_quality_assurance(self):
        self.scroll(self.careers_jobs_product_design)
        self.driver.find_element(*self.careers_jobs_quality_assurance).click()

    def is_quality_assurance_page_open(self) -> bool:
        return self.is_open(self.careers_jobs_quality_assurance_big_title)

    def click_on_see_all_qa_jobs(self):
        self.driver.find_element(*self.see_all_qa_jobs_button).click()

    def select_department(self, department: str):
        # 7 secs animation delay +1 for safety
        time.sleep(8)
        self.driver.find_element(*self.filter_by_department).click()
        self.is_department_list_present()
        dynamic_locator = (By.XPATH, f"//*[contains(@id, 'select2-filter-by-department-result-') and contains(@id, '{department}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dynamic_locator))
        self.driver.find_element(*dynamic_locator).click()

    def select_location(self, location: str):
        # 6 secs animation delay +1 for safety
        time.sleep(7)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.job_list_items))
        self.driver.find_element(*self.location).click()
        self.is_location_list_present()
        dynamic_locator = (By.XPATH, f"//*[contains(@id, 'select2-filter-by-location-result-') and contains(text(), '{location}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dynamic_locator))
        self.driver.find_element(*dynamic_locator).click()

    def get_selected_department(self) -> str:
        return self.driver.find_element(*self.filter_by_department).text

    def get_selected_location(self) -> str:
        return self.driver.find_element(*self.location).text

    def is_location_list_present(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.location_list))

    def is_department_list_present(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.filter_by_department_list))

    def is_job_list_present(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.job_list))

    def get_all_jobs(self):
        if not self.is_job_list_present():
            return None
        return self.driver.find_elements(*self.job_list_items)

    def get_job(self, position, department, location):
        job_items = self.get_all_jobs()
        for job in job_items:
            position_title = job.find_element(By.CLASS_NAME, "position-title").text
            department_title = job.find_element(By.CLASS_NAME, "position-department").text
            location_title = job.find_element(By.CLASS_NAME, "position-location").text
            if (
                    position == position_title and
                    department == department_title and
                    location == location_title
            ):
                return job
        return None

    def check_all_job_criteria(self, position, department, location):
        job_items = self.get_all_jobs()
        for job in job_items:
            position_title = job.find_element(By.CLASS_NAME, "position-title").text
            department_title = job.find_element(By.CLASS_NAME, "position-department").text
            location_title = job.find_element(By.CLASS_NAME, "position-location").text
            if (
                    position not in position_title or
                    department not in department_title or
                    location not in location_title
            ):
                return False
        return True

    def click_on_view_role(self, position, department, location):
        element = self.get_job(position, department, location)
        view_role_button = element.find_element(By.XPATH, "//*[text()='View Role']")
        self.scroll(self.bottom_pagination)
        self.hover_on_element(view_role_button)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(view_role_button))
        view_role_button.click()

    def is_redirected_on_lever(self) -> bool:
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains('jobs.lever.co/useinsider'))
        return "lever.co" in self.driver.current_url






