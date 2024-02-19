import sys
import pytest
from libs.helper import create_driver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from libs.constants import WEBDRIVER


@pytest.fixture()
def setup():
    os_browser_mapping = {
        "linux": ("firefox", "geckodriver_linux", FirefoxOptions),
        "darwin": ("chrome", "chromedriver_mac", ChromeOptions),
    }

    operating_system = next((os for os in os_browser_mapping if sys.platform.startswith(os)), None)
    if operating_system:
        browser, driver_name, OptionsClass = os_browser_mapping[operating_system]
        options = OptionsClass()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver_path = f"{WEBDRIVER}/{driver_name}"
        print(driver_path)
        driver = create_driver(browser, driver_path, options)
        yield driver
        driver.quit()
    else:
        raise ValueError(f"Unsupported operating system: {sys.platform}")
