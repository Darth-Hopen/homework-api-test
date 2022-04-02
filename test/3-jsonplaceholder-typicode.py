import pytest
import requests
from jsonschema import validate

base_url = "https://jsonplaceholder.typicode.com"


def test_api_json_schema():
    response = requests.get(url=base_url + "/albums/1")
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"},
            "userId": {"type": "number"}
        },
        "required": ["id", "title", "userId"]
    }
    validate(instance=response.json(), schema=schema)


def test_assert_email_count():
    expected = 0
    response = requests.get(url=base_url+"/posts/1/comments")
    json_dict = response.json()
    assert json_dict.count("test_test123@mail.ru") == expected


@pytest.mark.parametrize("filter_by, user_id", {
    ("posts", 1),
    ("todos", 5),
    ("albums", 3)
})
def test_filtering_resources(filter_by, user_id):
    response = requests.get(url=base_url + f"/{filter_by}?userId={user_id}")
    for item in response.json():
        assert item["userId"] == user_id


def test_get_albums_photo():
    albumId = 1
    response = requests.get(url=base_url+f"/albums/{albumId}/photos/")
    field = ["title", "url", "thumbnailUrl"]
    for item in response.json():
        assert item["albumId"] == albumId
    for item in field:
        assert item in response.json()[0].keys()


@pytest.mark.parametrize("input_body, expected_body",
                         [
                             ("test_body", "test_body"),
                             ("0", "0"),
                             ("test123", "test123")
                         ])
def test_assert_post_body(input_body, expected_body):
    response = requests.post(url=base_url+"/posts/", data={
        "title": input_body,
    }).json()
    assert response["title"] == expected_body
