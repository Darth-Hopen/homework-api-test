import requests


def test_url_and_status_code(url_and_code):
    response = requests.get(url=url_and_code["url"])
    assert str(response.status_code) == url_and_code["status_code"]
