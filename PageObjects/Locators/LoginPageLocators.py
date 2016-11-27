from selenium.webdriver.common.by import By


class LoginPageLocators(object):
	USERNAME_TEXTFIELD = (By.ID, 'Email')
	NEXT_BUTTON = (By.ID, 'next')
	PASSWORD_TEXTFIELD = (By.ID, 'Passwd')
	SIGNIN_BUTTON = (By.ID, 'signIn')
