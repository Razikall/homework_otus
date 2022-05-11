import pytest


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://ya.ru',
                     help='this is default true url')

    parser.addoption('--status_code',
                     default=200,
                     help='this is default true status code')


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_url(request):
    return int(request.config.getoption('--status_code'))
