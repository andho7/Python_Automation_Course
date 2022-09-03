import pytest
import requests


urls = [("https://www.aqa.science/admin/", 200),
        ("https://www.aqa.science/w_2.html", 200)]

url = "https://google.com"


def test_request_one(fixture_two):
    response = requests.get(urls[0][0])
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.smoke
def test_request_two():
    response = requests.get(urls[0][0])
    assert response.status_code == 200, f"Test response : {response.text}"


@pytest.mark.smoke
def test_request_three():
    response = requests.get(url)
    assert response.status_code == 200, f"Test response : {response.text}"


def test_google_home(fixture_two):
    url = 'https://google.com/'
    resp = requests.get(url)
    assert resp.status_code == 200
