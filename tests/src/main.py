import re
import string
import random
import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from src.locators import UsersPage, AdminPage, AddUserPage


class TestUser:
    def __init__(self, driver):
        self.username = self.set_username(driver)
        self.password = self.set_password(8)
        self.join_date = None
        self.user_id = None

    def set_username(self, driver: webdriver):
        username = f'user_name_test_{random.randint(1, 100)}'
        if self.is_user_exist(driver, username):
            username = f'user_name_test_{random.randint(1, 100)}'
        self.username = username
        return self.username

    @staticmethod
    def is_user_exist(driver: webdriver, username: str) -> bool:
        driver.get(f'https://www.aqa.science/admin/auth/user/')
        search_input = driver.find_element(By.ID, UsersPage.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(username)
        search_button = driver.find_element(By.XPATH, UsersPage.SEARCH_BUTTON)
        search_button.click()
        locator = UsersPage.USER_NAME_TEXT.format(username=username)
        time.sleep(2)
        try:
            username_web_elem = driver.find_element(By.XPATH, locator)
            if username_web_elem.text == username:
                return True
        except NoSuchElementException:
            return False

    def set_password(self, length):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        random.shuffle(characters)
        password = []
        for i in range(length):
            password.append(random.choice(characters))
        random.shuffle(password)
        self.password = "".join(password)
        return self.password

    def create_user(self, driver: webdriver):
        add_new_user_button = driver.find_element(By.XPATH, AdminPage.ADD_NEW_USER_BUTTON)
        add_new_user_button.click()

        username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = driver.find_element(By.ID, AddUserPage.PASSWORD_FIELD)
        password_field.send_keys(self.password)
        time.sleep(1)

        password_confirmation_field = driver.find_element(By.ID, AddUserPage.PASSWORD_CONFIRMATION_FIELD)
        password_confirmation = self.password
        password_confirmation_field.send_keys(password_confirmation)
        time.sleep(1)

        save_button = driver.find_element(By.XPATH, AddUserPage.SAVE_BUTTON)
        save_button.click()
        time.sleep(1)

        user_id = driver.current_url
        self.user_id = re.findall(r'\d+', user_id)[0]
        time.sleep(3)
        self.join_date = driver.find_element(By.ID, AddUserPage.DATE_TIME).get_attribute('value')

        time.sleep(1)
        save_edit_button = driver.find_element(By.XPATH, AddUserPage.SAVE_EDIT_BUTTON)
        time.sleep(1)
        save_edit_button.click()

    def get_user_join_time(self, driver: webdriver):
        if self.is_user_exist(driver, self.username):
            user_entity = driver.find_element(By.XPATH, UsersPage.USER_ENTITY)
            user_entity.click()
            time.sleep(1)
            self.join_date = driver.find_element(By.ID, AddUserPage.DATE_TIME).get_attribute('value')
            return self.join_date

    def is_username_equal(self, driver: webdriver):
        search_input = driver.find_element(By.ID, UsersPage.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(self.username)
        search_button = driver.find_element(By.XPATH, UsersPage.SEARCH_BUTTON)
        search_button.click()
        user_entity = driver.find_element(By.XPATH, UsersPage.USER_ENTITY)
        user_entity.click()

        username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
        username = username_field.get_attribute('value')
        return username == self.username

    def edit_username(self, driver: webdriver):
        if self.is_user_exist(driver, self.username):
            user_entity = driver.find_element(By.XPATH, UsersPage.USER_ENTITY)
            user_entity.click()
            time.sleep(1)
            username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
            username_field.clear()
            new_username = 'user_name_test_edited'
            username_field.send_keys(new_username)
            time.sleep(1)

            save_edit_button = driver.find_element(By.XPATH, AddUserPage.SAVE_EDIT_BUTTON)
            time.sleep(1)
            save_edit_button.click()
            self.username = new_username

    def delete_user(self, driver: webdriver):
        driver.get(f'https://www.aqa.science/admin/auth/user/{self.user_id}/change/')
        time.sleep(3)

        delete_button = driver.find_element(By.XPATH, AddUserPage.DELETE_BUTTON)
        delete_button.click()
        time.sleep(1)

        delete_confirmation_button = driver.find_element(By.XPATH, AddUserPage.DELETE_CONFIRMATION_BUTTON)
        delete_confirmation_button.click()
        return True



