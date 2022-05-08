import pytest

# Test api: https://jsonplaceholder.typicode.com/


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://jsonplaceholder.typicode.com',
                     help='request url')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')