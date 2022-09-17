import pytest


@pytest.mark.usefixtures("login_logout")
class TestAPI:
    def test_api_1(self):
        print('\ntesting ui.............')

    def test_api_2(self):
        print('\ntesting ui.............')