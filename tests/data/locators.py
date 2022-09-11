from selenium.webdriver.common.by import By


class LoginPage:
    SUBMIT_BUTTON = '//*[@id="login-form"]/div[3]/input'
    LOGIN_FIELD = 'id_username'
    PASSWORD_FILD = '//*[@id="id_password"]'


class AdminPage():
    PAGE_HEADER = '//*[@id="site-name"]/a'
    ADD_NEW_USER_BUTTON = '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'

class AddUserPage():
    USERNAME_FIELD = 'id_username'
    PASSWORD_FIELD = 'id_password1'
    PASSWORD_CONFIRMATION_FIELD = 'id_password2'
    SAVE_BUTTON = '//*[@id="user_form"]/div/div/input[1]'
    DATE_TIME = 'id_date_joined_1'
    DELETE_BUTTON = '//a[@class="deletelink"]'
    DELETE_CONFIRMATION_BUTTON = '//*[@id="content"]/form/div/input[2]'
    SAVE_EDIT_BUTTON = '//*[@id="user_form"]/div/div/input[1]'

class UsersPgae():
    SEARCH_BUTTON = '//*[@id="changelist-search"]/div/input[2]'
    SEARCH_INPUT = 'searchbar'
    USER_COUNT_FIELD = '//p[@class="paginator"]'
    USER_ENTITY = '//*[@id="result_list"]/tbody/tr/th/a'
