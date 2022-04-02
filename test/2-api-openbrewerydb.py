import pytest
import requests

base_url = "https://api.openbrewerydb.org"


def test_api_per_page():
    quantity = 5
    response = requests.get(url=base_url + "/breweries?per_page=" + str(quantity))
    assert len(response.json()) == quantity   


def test_get_all_breweries_list():
    response = requests.get(url=base_url + "/breweries")
    assert response.status_code == 200
    assert not len(response.json()) == 0


@pytest.mark.parametrize("query", ["dog", "cat", "bird"])
def test_api_search_query(query):
    response = requests.get(url=base_url + "/breweries/search", params={"query": query})
    assert query in response.text


@pytest.mark.parametrize("state", ["Indiana", "Oregon"])
def test_api_check_state(state):
    response = requests.get(url=base_url + "/breweries?by_city=" + state)
    for item in response.json():
        assert item["state"] == state


@pytest.mark.parametrize("b_type", ["micro", "nano"])
def test_filter_by_type_of_brewery(b_type):
    response = requests.get(url=base_url + "/breweries?by_type=" + b_type)
    for item in response.json():
        assert item["brewery_type"] == b_type
