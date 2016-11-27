from selenium import webdriver
import pytest


def open_browser():
    browser = pytest.config.getoption('--browser')

    if browser == 'chrome' or browser == 'Chrome':
        return webdriver.Chrome()

    elif browser == 'firefox' or browser == 'Firefox':
        return webdriver.Firefox()


def base_url():
    return pytest.config.getoption('--url')


def username():
    return pytest.config.getoption('--email')


def password():
    return pytest.config.getoption('--pass')