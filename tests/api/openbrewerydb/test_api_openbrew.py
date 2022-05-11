import pytest
import requests
from pydantic import BaseModel


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: str = None
    address_2: str = None
    address_3: str = None
    city: str
    state: str = None
    county_province: str = None
    postal_code: str
    country: str
    longitude: str = None
    latitude: str = None
    phone: str = None
    website_url: str = None
    updated_at: str
    created_at: str


class BreweryList(BaseModel):
    __root__: list[Brewery]


def validator(schema, obj):
    schema.parse_obj(obj)
    return True


def test_api(base_url):
    res = requests.get(base_url)
    assert res.ok
    assert validator(BreweryList, res.json())


def test_api_brewery(base_url):
    res = requests.get(base_url + "/madtree-brewing-cincinnati")
    assert res.ok
    assert validator(Brewery, res.json())


@pytest.mark.parametrize("i", ["Banjo_Brewing", "Bay_Brewing_Company", "devout-brewing-export"])
def test_api_by_name(base_url, i):
    res = requests.get(base_url + f"?by_name={i}")
    assert res.ok
    assert validator(BreweryList, res.json())


@pytest.mark.parametrize("i", ["Manchester", "Reedsburg", "Devout_Brewing"])
def test_api_by_city(base_url, i):
    res = requests.get((base_url + f"?by_city={i}"))
    assert res.ok
    assert validator(BreweryList, res.json())


@pytest.mark.parametrize("i", ["81416", "92648-1235"])
def test_api_by_postal(base_url, i):
    res = requests.get((base_url + f"?by_city={i}"))
    assert res.ok
    assert validator(BreweryList, res.json())
