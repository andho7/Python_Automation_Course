import random
import time
import re

from selenium.webdriver.common.by import By

from data.helpers import generate_random_password
from data.locators import LoginPage, AdminPage, AddUserPage, UsersPgae
from selenium import webdriver
import json


with open("data.json", "r") as f:
    secret_variables = json.load(f)

def login_to_admin_page(driver: webdriver):

    driver.get(secret_variables["endpoint"])

    name_field = driver.find_element(By.ID, LoginPage.LOGIN_FIELD)
    submit_button = driver.find_element(By.XPATH, LoginPage.SUBMIT_BUTTON)
    password_field = driver.find_element(By.XPATH, LoginPage.PASSWORD_FILD)

    name_field.send_keys(secret_variables["name"])
    time.sleep(1)
    password_field.send_keys(secret_variables["password"])

    submit_button.click()
    time.sleep(1)
    element_to_found = driver.find_element(By.XPATH, AdminPage.PAGE_HEADER)

    assert element_to_found.text == "Django administration"


def create_new_user(driver):
    add_new_user_button = driver.find_element(By.XPATH, AdminPage.ADD_NEW_USER_BUTTON)
    add_new_user_button.click()

    username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
    user_name = f'user_name_test_{random.randint(1,100)}'
    username_field.send_keys(user_name)
    time.sleep(1)

    password_field = driver.find_element(By.ID, AddUserPage.PASSWORD_FIELD)
    password = generate_random_password(8)
    password_field.send_keys(password)
    time.sleep(1)

    password_confirmation_field = driver.find_element(By.ID, AddUserPage.PASSWORD_CONFIRMATION_FIELD)
    password_confirmation = password
    password_confirmation_field.send_keys(password_confirmation)
    time.sleep(1)

    save_button = driver.find_element(By.XPATH, AddUserPage.SAVE_BUTTON)
    save_button.click()
    time.sleep(1)

    user_id = driver.current_url
    user_id = re.findall('\d+', user_id)
    time.sleep(3)
    join_date = driver.find_element(By.ID, AddUserPage.DATE_TIME).get_attribute('value')

    time.sleep(1)
    save_edit_button = driver.find_element(By.XPATH, AddUserPage.SAVE_EDIT_BUTTON)
    time.sleep(1)
    save_edit_button.click()

    data = {'username': user_name, 'password': password, 'user_id': user_id[0], 'date': join_date}
    with open('test_users.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return user_name

def is_user_found(user_name, driver) -> bool:
    driver.get(f'{secret_variables["endpoint"]}auth/user/')
    search_input = driver.find_element(By.ID, UsersPgae.SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(user_name)

    search_button = driver.find_element(By.XPATH, UsersPgae.SEARCH_BUTTON)
    search_button.click()

    return driver.find_element(By.XPATH, UsersPgae.USER_COUNT_FIELD).text == '1 user'

def get_user_join_time(user_name, driver):
    if is_user_found(user_name, driver):
        user_entity = driver.find_element(By.XPATH, UsersPgae.USER_ENTITY)
        user_entity.click()
        time.sleep(1)
        date_join_time = driver.find_element(By.ID, AddUserPage.DATE_TIME).get_attribute('value')
        return date_join_time

def edit_username(user_name, driver):
    if is_user_found(user_name, driver):
        user_entity = driver.find_element(By.XPATH, UsersPgae.USER_ENTITY)
        user_entity.click()
        time.sleep(1)
        username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
        username_field.clear()
        user_name = 'user_name_test_edited'
        username_field.send_keys(user_name)
        time.sleep(1)

        with open("test_users.json", 'r') as f:
            user = json.load(f)

        save_edit_button = driver.find_element(By.XPATH, AddUserPage.SAVE_EDIT_BUTTON)
        time.sleep(1)
        save_edit_button.click()

        user['username'] = user_name
        with open("test_users.json", 'w') as f:
            json.dump(user, f, ensure_ascii=False, indent=4)


def is_username(new_name, driver):
    search_input = driver.find_element(By.ID, UsersPgae.SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(new_name)
    search_button = driver.find_element(By.XPATH, UsersPgae.SEARCH_BUTTON)
    search_button.click()
    user_entity = driver.find_element(By.XPATH, UsersPgae.USER_ENTITY)
    user_entity.click()

    username_field = driver.find_element(By.ID, AddUserPage.USERNAME_FIELD)
    username = username_field.get_attribute('value')
    if username == new_name:
        return True


def delete_user(user_id, driver):
    driver.get(f'{secret_variables["endpoint"]}auth/user/{user_id}/change/')
    time.sleep(1)

    delete_button = driver.find_element(By.XPATH, AddUserPage.DELETE_BUTTON)
    delete_button.click()
    time.sleep(1)


    delete_confirmation_button = driver.find_element(By.XPATH, AddUserPage.DELETE_CONFIRMATION_BUTTON)
    delete_confirmation_button.click()
