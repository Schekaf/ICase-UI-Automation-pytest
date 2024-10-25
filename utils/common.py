from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Common:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, locator: tuple):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def is_open(self, locator) -> bool:
        try:
            # Wait until an element is present in the DOM and visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def hover_on_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
