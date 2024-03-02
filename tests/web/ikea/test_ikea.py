import allure
from allure_commons.types import AttachmentType

from tests.web.ikea.pom.home_page import HomePage


class TestIkea:
    def test_title(self, setup, host):
        home_page = HomePage(setup, host)
        assert home_page.get_title() == "1Frische Einrichtungsideen & erschwingliche Möbel - IKEA Deutschland"
        print(home_page.get_title())
