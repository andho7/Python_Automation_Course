import json
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.locators import AdminPage, LoginPage

base_dir = Path(__file__).parent.parent

with open(f"{base_dir}/data.json", "r") as f:
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


def logout(driver: webdriver):
    driver.get(f'{secret_variables["endpoint"]}logout/')
