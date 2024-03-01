from libs.helper import SingletonMeta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(metaclass=SingletonMeta):
    TITLE = "head > title"

    def __init__(self, setup, url):
        self.driver = setup
        self.driver.get(url)

    def get_title(self):
        self.driver.implicitly_wait(5)
        return self.driver.execute_script(f"return document.querySelector('{self.TITLE}').textContent;")
