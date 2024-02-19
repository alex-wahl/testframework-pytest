from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver(browser, driver_path, options):
    if browser == "firefox":
        return webdriver.Firefox(service=Service(driver_path), options=options)
    elif browser == "chrome":
        return webdriver.Chrome(service=Service(driver_path), options=options)
