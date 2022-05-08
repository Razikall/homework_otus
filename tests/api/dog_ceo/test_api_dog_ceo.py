import pytest
import requests
from jsonschema import validate

schema = {
    "type": "object",
    "required": ["message", "status"],
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
}

schema_with_params = {
    "type": "object",
    "required": ["message", "status"],
    "properties": {
        "status": {"type": "string"},
        "message": {
            "type": "array",
            "items": {"type": "string"},
        }
    }
}


def validator(obj, current_json):
    validate(obj, current_json)
    return True


def test_api(base_url):
    res = requests.get(base_url)
    assert res.ok
    assert res.encoding == 'UTF-8'


def test_api_random(base_url):
    res = requests.get(base_url + "/breeds/image/random")
    assert res.ok
    assert validator(res.json(), current_json=schema)


@pytest.mark.parametrize('i', range(1, 4))
def test_api_random_all(base_url, i):
    res = requests.get(base_url + f"/breeds/image/random/{i}")
    assert res.ok
    assert validator(res.json(), current_json=schema_with_params)


def test_api_sub_breed(base_url):
    res = requests.get(base_url + "/breed/hound/list")
    assert res.ok
    assert validator(res.json(), current_json=schema_with_params)


@pytest.mark.parametrize('i', range(1, 4))
def test_api_random_images(base_url, i):
    res = requests.get(base_url + f"/breed/affenpinscher/images/random/{i}")
    assert res.ok
    assert validator(res.json(), current_json=schema_with_params)
