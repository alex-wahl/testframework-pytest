import sys

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

from libs.constants import WEBDRIVER


@pytest.fixture()
def setup():
    os_driver_mapping = {
        "linux": "chromedriver_linux",
        "darwin": "chromedriver_mac",
        "win32": "geckodriver"
    }
    operating_system = next(
        (operating_system for operating_system in os_driver_mapping if sys.platform.startswith(operating_system)), None)

    # Setup options
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

    if operating_system:
        driver_path = f"{WEBDRIVER}/{os_driver_mapping[operating_system]}"
        print(driver_path)
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
        yield driver
        driver.quit()
    else:
        raise ValueError(f"Unsupported operating system: {sys.platform}")
