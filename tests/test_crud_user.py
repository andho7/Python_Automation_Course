from data.base_page import login_to_admin_page, create_new_user, is_user_found, get_user_join_time
import json


def test_create_user(driver):
    login_to_admin_page(driver)
    create_new_user(driver)
    with open("test_users.json", "r") as f:
        user = json.load(f)
    assert is_user_found(user['username'], driver)

def test_get_user_join_time(driver):
    login_to_admin_page(driver)
    create_new_user(driver)
    with open("test_users.json", "r") as f:
        user = json.load(f)
    assert get_user_join_time(user['username'], driver) == user['date']

def test_edit_user_info(driver):
    pass
def test_delete_user(driver):
    pass