import pytest

from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/api_scenarios.feature')


@when("I create a new user", target_fixture='create_user')
def create_user(api):
    username = api.generate_username()
    assert not api.is_username(username)
    api.create_user(username)
    return username


@then("I ensure that username can be found in user's list")
def ensure_that_user_created(api, create_user):
    assert api.is_username(create_user)


@then("I ensure that username can NOT be found in user's list")
def ensure_that_user_created(api):
    assert not api.is_username(api.username)


@then("I ensure that user data is equal to data for created user")
def ensure_that_user_data_equal(api):
    assert api.is_user_data_equal()


@when("I update username")
def update_username(api):
    api.update_username()


@when("I delete newly created user")
@then("I delete newly created user")
def delete_user(api):
    api.delete_user()
