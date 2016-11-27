import pytest
import config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome',
                     help="my option: chrome or firefox")
    parser.addoption("--url", action="store", default='https://calendar.google.com/',
                     help="base url of the application")

    parser.addoption("--email", action="store", default=config.username,
                     help="email used for logging in")

    parser.addoption("--pass", action="store", default=config.password,
                     help="password used for logging in")