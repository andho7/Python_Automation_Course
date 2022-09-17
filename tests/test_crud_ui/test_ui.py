import pytest

from src.main import TestUser


@pytest.mark.usefixtures("login_logout")
class TestUI:

    def test_create_user(self, driver):
        user = TestUser(driver)
        user.create_user(driver)
        assert user.is_user_exist(driver, user.username)
        user.delete_user(driver)

    def test_check_user_info(self, driver):
        user = TestUser(driver)
        user.create_user(driver)
        assert user.is_username_equal(driver)
        assert user.join_date == user.get_user_join_time(driver)
        user.delete_user(driver)

    def test_edit_user_join_date(self, driver):
        user = TestUser(driver)
        user.create_user(driver)
        user.edit_username(driver)
        assert user.is_username_equal(driver)
        user.delete_user(driver)

    def test_delete_user(self, driver):
        user = TestUser(driver)
        user.create_user(driver)
        user.delete_user(driver)
        assert not user.is_user_exist(driver, user.username)
