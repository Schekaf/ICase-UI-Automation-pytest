from selenium.webdriver.common.by import By

from utils.common import Common


class OpenPositionsPage(Common):

    # Locators
    filter_by_location = (By.ID, "select2-filter-by-location-container")
    istanbul_turkey_filter = (By.ID, "select2-filter-by-location-result-8l46-Istanbul, Turkey")