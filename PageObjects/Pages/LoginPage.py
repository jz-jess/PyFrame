from PageObjects.Locators.LoginPageLocators import LoginPageLocators
from time import sleep
from BasePage import BasePage
from CalendarPage import CalendarPage


class LoginPage(BasePage):
    def go_to_page(self, base_url):
        self.go_to(base_url)

    def login(self, username, password):
        self.enter_text(LoginPageLocators.USERNAME_TEXTFIELD, username)
        self.click_element(LoginPageLocators.NEXT_BUTTON)
        sleep(1)
        self.enter_text(LoginPageLocators.PASSWORD_TEXTFIELD, password)
        self.click_element(LoginPageLocators.SIGNIN_BUTTON)
        return CalendarPage(self.driver)
