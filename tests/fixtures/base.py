import sys

import allure
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from libs.helper import clean_up, create_driver


@pytest.fixture()
def setup():
    os_browser_mapping = {
        "linux": ("firefox", FirefoxOptions),
        "darwin": ("chrome", ChromeOptions),
    }

    operating_system = next((os for os in os_browser_mapping if sys.platform.startswith(os)), None)
    if operating_system:
        browser, OptionsClass = os_browser_mapping[operating_system]
        options = OptionsClass()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = create_driver(browser, options)
        yield driver
        driver.quit()
        clean_up()
    else:
        raise ValueError(f"Unsupported operating system: {sys.platform}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        try:
            if 'setup' in item.fixturenames:
                web_driver = item.funcargs['setup']
            else:
                print('Driver not found in test.')
                return
            screenshot = web_driver.get_screenshot_as_png()
            allure.attach(screenshot, name='screenshot', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Failed to capture screenshot: {e}')
