import pytest

from pages.home_page import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver

class TestCrud:

    def test_one(self):
        assert True

    def test_home_page(self, driver: WebDriver):
        assert HomePage(driver).is_log_in_button_visible()