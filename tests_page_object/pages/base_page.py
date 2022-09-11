from typing import Tuple

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as AC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator:'Tuple[By, str]', timeout: float=10) -> 'bool | WebElement':
        elem: WebElement = None
        try:
            elem = WebDriverWait(
                self.driver, timeout).until(AC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        print(f'{elem.text} is found')
        return elem

    def find_element_and_click(self):
        pass