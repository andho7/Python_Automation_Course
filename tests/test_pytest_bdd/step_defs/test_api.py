from pytest_bdd import scenarios, when, then

scenarios('../features/api_scenarios.feature')


@when("I create a new user")
def create_user(api):
    """
    Create a new user account
    """
    username = api.generate_username()
    assert not api.is_username(username)
    api.create_user(username)


@then("I ensure that username can be found in user's list")
def ensure_that_user_created(api):
    """
    Check if username is found in users list
    """
    assert api.is_username(api.username)


@then("I ensure that username can NOT be found in user's list")
def ensure_that_user_created(api):
    """
    Check if username is NOT found in users list
    """
    assert not api.is_username(api.username)


@then("I ensure that user data is equal to data for created user")
def ensure_that_user_data_equal(api):
    """
    Check if user data is equal to data for created user
    """
    assert api.is_user_data_equal()


@when("I update username")
def update_username(api):
    """
    Update username
    """
    api.update_username()


@when("I delete newly created user")
@then("I delete newly created user")
def delete_user(api):
    """
    Delete user account
    """
    api.delete_user()
