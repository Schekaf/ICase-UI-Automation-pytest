from selenium.webdriver.common.by import By

from utils.common import Common


class QualityAssurancePage(Common):

    # Locators
    see_all_jobs_button = (By.XPATH, "//*[contains(@class,'btn') and contains(text(), 'See all QA jobs')]")

