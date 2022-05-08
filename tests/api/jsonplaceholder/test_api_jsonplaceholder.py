import requests
import pytest
from pydantic import BaseModel, HttpUrl


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PostsList(BaseModel):
    __root__: list[Post]


class Album(BaseModel):
    userId: int
    id: int
    title: str


class AlbumsList(BaseModel):
    __root__: list[Album]


class Photo(BaseModel):
    albumId: int
    id: int
    title: str
    url: HttpUrl
    thumbnailUrl: HttpUrl


class PhotosList(BaseModel):
    __root__: list[Photo]


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class UsersList(BaseModel):
    __root__: list[User]


def validator(schema, obj):
    schema.parse_obj(obj)
    return True


@pytest.mark.parametrize('i', range(1, 4))
def test_api_post(base_url, i):
    res = requests.get(base_url + f"/posts/{i}")
    assert res.ok
    assert validator(Post, res.json())


def test_api_posts_all(base_url):
    res = requests.get(base_url + "/posts")
    assert res.ok
    assert validator(PostsList, res.json())


@pytest.mark.parametrize('i', range(1, 4))
def test_api_album_photos(base_url, i):
    res = requests.get(base_url + f"/albums/{i}/photos")
    assert res.ok
    assert validator(PhotosList, res.json())


def test_api_all_albums(base_url):
    res = requests.get(base_url + "/albums")
    assert res.ok
    assert validator(AlbumsList, res.json())


def test_api_users(base_url):
    res = requests.get(base_url + "/users")
    assert res.ok
    assert validator(UsersList, res.json())


@pytest.mark.parametrize('i', range(1, 4))
def test_api_user_albums(base_url, i):
    res = requests.get(base_url + f"/users/{i}/albums")
    assert res.ok
    assert validator(AlbumsList, res.json())
