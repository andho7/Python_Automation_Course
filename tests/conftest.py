"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
import json
import re

import pytest
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from src.auth import login_to_admin_page, logout, WebAPI


@pytest.fixture(scope='session')
def driver() -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    print('WebDriver is created')
    yield driver
    driver.close()
    print('\nWebDriver is closed')


@pytest.fixture(scope='class')
def login_logout(driver):
    login_to_admin_page(driver)
    print('User is logged in to Admin panel')
    yield driver
    logout(driver)
    print('\nUser is logged out from Admin panel')


@pytest.fixture(scope='class')
def api():
    admin_session = WebAPI()
    admin_session.login()
    yield admin_session
    admin_session.logout()


# r2 = s.get('https://www.aqa.science/users/1291')
# print(r2.json())
#
# data = {
#     "url": "https://www.aqa.science/users/1291/",
#     "username": "user111_2_1+1+6",
#     "email": "",
#     "groups": []
# }
# a = json.dumps(data, indent=4)
# r2 = s.get(url='https://www.aqa.science/users/1291/',
#            headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
#                               'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}).text
# csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
#
# r4 = s.put(url='https://www.aqa.science/users/1291/',
#            data=a,
#            headers={'Content-Type': 'application/json',
#                     'X-CSRFTOKEN': csrf,
#                     'Referer': 'https://www.aqa.science/users/1291/'})
# print(r4.request.headers)
# print(r4.request.body)
# print(r4.request.method)
# print(r4.status_code)
# print(r4.text)
