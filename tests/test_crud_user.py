from data.base_page import login_to_admin_page, create_new_user, is_user_found, get_user_join_time, edit_username, \
    is_username, delete_user
import json


class TestCRUD:

    @staticmethod
    def get_json_data():
        with open("test_users.json", "r") as f:
            user = json.load(f)
        return user

    def test_create_user(self, driver):
        create_new_user(driver)
        user = self.get_json_data()
        assert is_user_found(user['username'], driver)

    def test_get_user_join_time(self, driver):
        create_new_user(driver)
        user = self.get_json_data()
        assert get_user_join_time(user['username'], driver) == user['date']

    def test_edit_user_info(self, driver):
        create_new_user(driver)
        user = self.get_json_data()
        edit_username(user['username'], driver)
        assert is_username('user_name_test_edited', driver)

    def test_delete_user(self, driver):
        create_new_user(driver)
        user = self.get_json_data()
        try:
            is_user_found(user['username'], driver)
            delete_user(user['user_id'], driver)
        except RuntimeError as err:
            print(err)
        assert not is_user_found(user['username'], driver)
