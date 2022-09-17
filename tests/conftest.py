"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""

import pytest
from selenium import webdriver

from src.auth import login_to_admin_page, logout


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
