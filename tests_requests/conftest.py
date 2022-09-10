import pytest as pytest


@pytest.fixture(scope='class', autouse=True)
def fixture_one():
    print("\nStart tests")
    yield
    print("\nFinish tests ")


@pytest.fixture(scope='session')
def fixture_two():
    yield
    print("Post conditions")
