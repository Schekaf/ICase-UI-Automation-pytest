from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    logo = (By.XPATH, "//*[@alt='insider_logo']")
    company = (By.XPATH, "//*[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    company_careers = (By.XPATH, "//*[@class='dropdown-sub' and contains(text(), 'Careers')]")

    def wait_logo_to_be_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logo))

    def click_company(self):
        self.driver.find_element(*self.company).click()

    def click_company_careers(self):
        self.driver.find_element(*self.company_careers).click()
