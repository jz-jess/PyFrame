from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self, 10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def go_to(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def findall(self, locator):
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(str(text))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def select_dropdown_by_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)
