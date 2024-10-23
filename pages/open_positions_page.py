from selenium.webdriver.common.by import By


class OpenPositionsPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    filter_by_location = (By.ID, "select2-filter-by-location-container")
    istanbul_turkey_filter = (By.ID, "select2-filter-by-location-result-8l46-Istanbul, Turkey")