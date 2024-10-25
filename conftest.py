import pytest
from utils.browser import get_driver
from utils.common import Common


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = get_driver(browser_name)  # Initialize the WebDriver based on the browser name
    driver.get("https://useinsider.com/")
    yield driver
    driver.quit()


