from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    jobs_list = ["Customer Success",
                 "Sales",
                 "Product & Engineering",
                 "Finance & Business Support",
                 "Marketing",
                 "CEO’s Executive Office",
                 "Purchasing & Operations",
                 "People and Culture",
                 "Business Intelligence",
                 "Security Engineering",
                 "Partnership",
                 "Quality Assurance",
                 "Mobile Business Unit",
                 "Partner Support Development",
                 "Product Design"
                 ]
    locations_list = ['New York\nUS', 'Sao Paulo\nBrazil', 'London\nUnited Kingdom', 'Paris\nFrance', 'Amsterdam\nNetherlands', 'Barcelona\nSpain', 'Helsinki\nFinland', 'Warsaw\nPoland', 'Kiev\nUkraine', 'Moscow\nRussia', 'Sydney\nAustralia', 'Dubai\nUnited Arab Emirates', 'Tokyo\nJapan', 'Seoul\nKorea', 'Singapore\nSingapore', 'Bangkok\nThailand', 'Jakarta\nIndonesia', 'Taipei\nTaiwan', 'Manila\nPhilippines', 'Kuala Lumpur\nMalaysia', 'Ho Chi Minh City\nVietnam', 'Istanbul\nTurkey', 'Ankara\nTurkey', 'Mexico City\nMexico', 'Lima\nPeru', 'Buenos Aires\nArgentina', 'Bogota\nColombia', 'Santiago\nChile']
    careers_jobs = (By.XPATH, "//*[contains(@class, 'job-title')]")
    careers_locations = (By.XPATH, "//*[contains(@class, 'location-info')]")
    careers_locations_move_right = (By.XPATH, "//*[contains(@class,'icon-arrow-right')]")
    careers_location_progress_bar = (By.XPATH, "//*[@class='progress']")
    careers_life_at_Insider = (By.XPATH, "//*[@data-id='21cea83']")

    def wait_careers_page_to_be_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.careers_jobs))

    def get_locations(self) -> [str]:
        actual_locations = []
        progress_bar = self.driver.find_element(*self.careers_location_progress_bar)
        locations_move_right = self.driver.find_element(*self.careers_locations_move_right)
        # Scroll to the element
        ActionChains(self.driver).move_to_element(progress_bar).perform()
        progress = 0
        while progress < 60:
            elements = self.driver.find_elements(*self.careers_locations)
            for element in elements:
                if not element.text in actual_locations and element.text != '' and "\n" in element.text:
                    actual_locations.append(element.text)
            locations_move_right.click()
            progress_bar = self.driver.find_element(*self.careers_location_progress_bar)
            progress = float(progress_bar.get_attribute('style').replace('width: ', '').replace('%;', ''))
        return actual_locations
