from pom.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    COOCKIES_BANNER_ACCEPT_BUTTON = "onetrust-accept-btn-handler"

    def accept_coockies(self):
        self.wait_until_element_is_visible(By.ID, self.COOCKIES_BANNER_ACCEPT_BUTTON)
        self.click_element(By.ID, self.COOCKIES_BANNER_ACCEPT_BUTTON)
