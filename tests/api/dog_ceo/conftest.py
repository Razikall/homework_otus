import pytest

# Test api: https://dog.ceo/api


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://dog.ceo/api',
                     help='request url')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
