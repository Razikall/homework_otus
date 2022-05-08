import requests


def test_responce(url, status_url):
    assert requests.get(url).status_code == status_url
