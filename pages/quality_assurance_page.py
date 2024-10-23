from selenium.webdriver.common.by import By


class QualityAssurancePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    see_all_jobs_button = (By.XPATH, "//*[contains(@class,'btn') and contains(text(), 'See all QA jobs')]")

