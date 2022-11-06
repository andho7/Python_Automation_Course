from pytest_bdd import scenarios, given, when, then, parsers

from src.main import TestUser

scenarios('../features/ui_scenarios.feature')


@when("I create a new user", target_fixture="create_user")
def create_user(login_logout, request):
    """
    Create a new user account
    """
    user = TestUser(login_logout)
    user.create_user(login_logout)
    assert user.is_user_exist(login_logout, user.username)
    return user


@then("I ensure that username can be found in user's list")
def ensure_that_user_created(login_logout, create_user):
    """
    Check if username is found in users list
    """
    user = create_user
    assert user.is_user_exist(login_logout, user.username)


@then("I ensure that username can NOT be found in user's list")
def ensure_that_user_created(login_logout, create_user):
    """
    Check if username is NOT found in users list
    """
    user = create_user
    assert not user.is_user_exist(login_logout, user.username)


@then("I ensure that user data is equal to data for created user")
def ensure_that_user_data_equal(login_logout, create_user):
    """
    Check if user data is equal to data for created user
    """
    user = create_user
    assert user.is_username_equal(login_logout)
    assert user.join_date == user.get_user_join_time(login_logout)


@when("I update username")
def update_username(login_logout, create_user):
    """
    Update username
    """
    user = create_user
    user.edit_username(login_logout)


@when("I delete newly created user")
@then("I delete newly created user")
def delete_user(login_logout, create_user):
    """
    Delete user account
    """
    user = create_user
    user.delete_user(login_logout)