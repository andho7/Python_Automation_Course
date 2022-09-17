class LoginPage:
    SUBMIT_BUTTON = '//*[@id="login-form"]/div[3]/input'
    LOGIN_FIELD = 'id_username'
    PASSWORD_FILD = '//*[@id="id_password"]'


class AdminPage:
    PAGE_HEADER = '//*[@id="site-name"]/a'
    ADD_NEW_USER_BUTTON = '//*[@id="nav-sidebar"]//tr[2]//a[text()="Add"]'


class AddUserPage:
    USERNAME_FIELD = 'id_username'
    PASSWORD_FIELD = 'id_password1'
    PASSWORD_CONFIRMATION_FIELD = 'id_password2'
    SAVE_BUTTON = '//*[@id="user_form"]/div/div/input[1]'
    DATE_TIME = 'id_date_joined_1'
    DELETE_BUTTON = '//a[@class="deletelink"]'
    DELETE_CONFIRMATION_BUTTON = '//*[@id="content"]/form/div/input[2]'
    SAVE_EDIT_BUTTON = '//*[@id="user_form"]/div/div/input[1]'


class UsersPage:
    SEARCH_BUTTON = '//*[@id="changelist-search"]/div/input[2]'
    SEARCH_INPUT = 'searchbar'
    USER_NAME_TEXT = "//*[@id='result_list']//a[text()='{username}']"
    USER_ENTITY = '//*[@id="result_list"]/tbody/tr/th/a'
