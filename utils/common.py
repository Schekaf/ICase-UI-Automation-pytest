from selenium.webdriver import ActionChains


class Common:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, locator: tuple):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()
