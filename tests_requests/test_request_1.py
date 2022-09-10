import pytest
import requests


@pytest.fixture(scope="class", autouse=True)
def fixture_two():
    print("Class fixture on start")
    yield
    print("Class fixture on end")


class TestRequestOne:
    urls = [("https://www.aqa.science/admin/", 200),
            ("https://www.aqa.science/w_2.html", 200)]

    url = "https://google.com"

    def test_request_one(self):
        response = requests.get(self.urls[0][0])
        assert response.status_code == 200, f"Test response : {response.text}"

    @pytest.mark.smoke
    def test_request_two(self):
        response = requests.get(self.urls[0][0])
        assert response.status_code == 200, f"Test response : {response.text}"

    @pytest.mark.smoke
    def test_request_three(self):
        response = requests.get(self.url)
        assert response.status_code == 200, f"Test response : {response.text}"
