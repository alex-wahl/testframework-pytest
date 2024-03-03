from pom.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    COOCKIES_BANNER = "onetrust-banner-sdk"
    COOCKIES_BANNER_ACCEPT_BUTTON = "onetrust-accept-btn-handler"
    COOCKIES_BANNER_ACCEPT_BUTTON_SELECTOR = f"#{COOCKIES_BANNER_ACCEPT_BUTTON}"

    def accept_coockies(self):
        self.wait_until_element_is_visible(self.COOCKIES_BANNER)
        self.click_element(By.ID, self.COOCKIES_BANNER_ACCEPT_BUTTON)
