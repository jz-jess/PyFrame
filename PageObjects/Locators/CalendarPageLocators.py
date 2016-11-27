from selenium.webdriver.common.by import By


class CalendarPageLocators(object):
    PROFILE_PIC = (By.CSS_SELECTOR, '.gb_8a.gbii')
    SETTINGS_BUTTON = (By.ID, 'mg-settings')
    CALENDAR_TIMINGS = (By.CSS_SELECTOR, '.tg-times-pri > div[style="height:42px;"] > .tg-time-pri')
    FIRST_WEEKDAY = (By.CSS_SELECTOR, '.wk-daynames > th > div.wk-dayname > span')
