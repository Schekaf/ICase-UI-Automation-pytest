from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on: chrome or firefox"
    )


def get_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.cookies": 2,  # 2 = Block all cookies
            "profile.block_third_party_cookies": True  # Block third-party cookies
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("network.cookie.cookieBehavior", 2)
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    return driver
