import pytest
import requests
from jsonschema import validate

base_url = "https://dog.ceo/api"


def test_api_status_code():
    response = requests.get(url=base_url + "/breeds/list/all")
    assert response.status_code == 200
    assert not len(response.json()["message"]) == 0


def test_api_json_scheme():
    response = requests.get(url=base_url + "/breeds/image/random")
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("n", [1, 99])
@pytest.mark.parametrize("breed", ["bouvier", "corgi", "samoyed"])
def test_get_multiple_random_images_by_breed(n, breed):
    response = requests.get(url=base_url + f"/breed/{breed}/images/random/{n}")
    assert response.status_code == 200
    assert len(response.json()["message"]) == n
    for obj in response.json()["message"]:
        assert ("images" in obj) and (f"{breed}" in obj)


@pytest.mark.parametrize("breed, sub_bread_exists", [("hound", True), ("bulldog", True), ("chihuahua", False)])
def test_api_check_sub_breed(breed, sub_bread_exists):
    response = requests.get(url=base_url + f"/breed/{breed}/list")
    if sub_bread_exists:
        assert len(response.json()["message"]) > 0
    else:
        assert len(response.json()["message"]) == 0


def test_api_json_not_empty():
    response = requests.get(url=base_url + "/breeds/image/random")
    assert response.json() != []
