from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver(browser, driver_path, options):
    if browser == "firefox":
        return webdriver.Firefox(service=Service(driver_path), options=options)
    elif browser == "chrome":
        return webdriver.Chrome(service=Service(driver_path), options=options)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
