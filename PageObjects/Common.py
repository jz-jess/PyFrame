
import pytest


def base_url():
    return pytest.config.getoption('--url')


def username():
    return pytest.config.getoption('--email')


def password():
    return pytest.config.getoption('--pass')