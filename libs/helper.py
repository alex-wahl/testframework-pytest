import pathlib
from functools import wraps

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

    @staticmethod
    def reset_instance(cls):
        if cls in cls._instances:
            del cls._instances[cls]


def reset_singleton_after_test(cls):
    def decorator(test_func):
        @wraps(test_func)
        def wrapper(*args, **kwargs):
            try:
                # Execute the test function
                result = test_func(*args, **kwargs)
            finally:
                # Ensure the singleton instance is reset after the test
                SingletonMeta.reset_instance(cls)
            return result

        return wrapper

    return decorator
