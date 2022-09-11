"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900
 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
import json
import pytest
from selenium import webdriver

from data.base_page import is_user_found, delete_user


@pytest.fixture(scope='session', autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    yield driver

    # with open("test_users.json", "r") as f:
    #     user = json.load(f)
    # if is_user_found(user['username'], driver):
    #     delete_user(user['user_id'], driver)

    driver.close()
