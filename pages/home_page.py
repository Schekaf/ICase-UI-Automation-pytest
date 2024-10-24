from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    company = (By.XPATH, "//*[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    company_careers = (By.XPATH, "//*[@class='dropdown-sub' and contains(text(), 'Careers')]")

    def click_company(self):
        self.driver.find_element(*self.company).click()

    def click_company_careers(self):
        self.driver.find_element(*self.company_careers).click()