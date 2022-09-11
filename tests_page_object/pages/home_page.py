from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):

    def is_log_in_button_visible(self):
        return self.find_element(HomePageLocators.LOGIN_BUTTON)