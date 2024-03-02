import sys
import pytest
from libs.helper import create_driver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


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
    else:
        raise ValueError(f"Unsupported operating system: {sys.platform}")
