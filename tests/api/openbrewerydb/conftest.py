import pytest

# Test api: https://www.api.openbrewerydb.org


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://api.openbrewerydb.org/breweries',
                     help='request url')


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
