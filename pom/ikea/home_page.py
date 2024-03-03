from pom.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    COOCKIES_BANNER_ACCEPT_BUTTON = "onetrust-accept-btn-handler"
    SEARCH_ID_FIELD = "ikea-search-input"
    SEARCH_SUMMARY_CLASS = "search-summary__heading b"

    def accept_coockies(self):
        self.wait_until_element_is_visible(By.ID, self.COOCKIES_BANNER_ACCEPT_BUTTON)
        self.click_element(By.ID, self.COOCKIES_BANNER_ACCEPT_BUTTON)

    def search_for(self, search_phrase: str):
        self.accept_coockies()
        self.wait_until_element_is_visible(By.ID, self.SEARCH_ID_FIELD)
        self.driver.find_element(By.ID, self.SEARCH_ID_FIELD).send_keys(search_phrase)
        self.driver.find_element(By.ID, self.SEARCH_ID_FIELD).submit()

    def get_search_summary(self):
        self.wait_until_element_is_visible(By.CLASS_NAME, self.SEARCH_SUMMARY_CLASS)
        return self.driver.find_element(By.CLASS_NAME, self.SEARCH_SUMMARY_CLASS).text
