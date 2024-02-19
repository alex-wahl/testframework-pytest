import pytest

from libs.constants import Environment


def pytest_addoption(parser):
    parser.addoption("--env", required=False, default=Environment.PROD.name, choices=[env.name for env in Environment])
    parser.addoption("--user", required=False, action="store", default=None, type=str,
                     help="Required to define a particular test configuration")
    parser.addoption("--password", required=False, action="store", default=None, type=str,
                     help="Required to define a particular test configuration")


@pytest.fixture(scope='session')
def host(request):
    """
    Fetches the host based on cli information.
    :param request: pytest fixture request for command-line options.
    :return: A string of the host like https://ikea.com or https://qa.ikea.com
    """
    return Environment[request.config.getoption('--env')].value


@pytest.fixture(scope='session')
def credentials(request) -> dict:
    """
    Fetches credentials based on cli information.
    :param request: pytest fixture request for command-line options.
    :return: A dictionary of user credentials.
    """

    return {
        'user': request.config.getoption("login"),
        'password': request.config.getoption("password")
    }
