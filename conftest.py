import datetime
import os

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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run the test
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        # Take a screenshot if the test failed
        screenshot_dir = 'screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)  # Create directory if it doesn't exist

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")

        # Get the driver from the current test context
        driver = item.funcargs['driver']
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

