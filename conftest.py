import pytest, os
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            test_func = _get_test_func(item.obj)
            ss_path = take_failed_ss(test_func.driver)
            extra.append(pytest_html.extras.html('<img src="%s">' % ss_path))
        report.extra = extra


@pytest.yield_fixture
def driver(request):
    browser = pytest.config.getoption('--browser')
    from selenium import webdriver
    if browser == 'chrome' or browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox' or browser == 'Firefox':
        driver = Firefox()
    request.instance.driver = driver
    yield driver
    driver.quit()



@pytest.fixture(scope='function', autouse=True)
def set_driver_to_test_for_failed_screenshot(request, driver):
    _get_test_func(request.node.obj).driver = driver


def _get_test_func(obj):
    # Test function may be method. But attributes can be set only to functions.
    if hasattr(obj, 'im_func'):
        return obj.im_func
    return obj


def take_failed_ss(driver):
    curdir = os.getcwd()
    directory = curdir + '/screenshots'
    if not os.path.exists(directory):
        os.makedirs(directory)
    count = 1
    while True:
        if not os.path.exists(directory + '/img' + str(count) + '.png'):
            ss_name = '/img' + str(count) + '.png'
            break
        count += 1
    driver.save_screenshot(directory + ss_name)
    return directory + ss_name

