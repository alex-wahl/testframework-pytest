import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser: str, options: webdriver.ChromeOptions or webdriver.FirefoxOptions):
    if browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def clean_up():
    for file in pathlib.Path().iterdir():
        if file.suffix == ".jpg" or file.suffix == ".png":
            file.unlink()


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
