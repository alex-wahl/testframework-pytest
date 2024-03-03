from pom.ikea.home_page import HomePage
import allure


class TestIkea:
    @allure.title("Ikea Home Page Title Test")
    def test_title(self, setup, host):
        home_page = HomePage(setup, host)
        home_page.wait_until_page_is_fully_loaded()
        assert home_page.get_title() == "Frische Einrichtungsideen & erschwingliche Möbel - IKEA Deutschland"
        print(home_page.get_title())
        home_page.make_screenshot()

    @allure.title("Ikea Accept Cookies")
    def test_coockies(self, setup, host):
        home_page = HomePage(setup, host)
        home_page.wait_until_page_is_fully_loaded()
        home_page.accept_coockies()
        home_page.make_screenshot()
