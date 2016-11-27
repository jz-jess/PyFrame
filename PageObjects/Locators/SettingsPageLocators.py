from selenium.webdriver.common.by import By


class SettingsPageLocators(object):
    CALENDARPAGE_LINK = (By.XPATH, '//*[@id="sbodyheader"]/th/div/div/span/b')
    TIME_FORMAT_DRODPDOWN = (By.ID, 'format24HourTime')
    SAVE_BUTTON = (By.ID, 'settings_save_btn')
    WEEK_START_DROPDOWN = (By.ID, 'firstDay')
    SPEEDY_MEETING_CHECKBOX = (By.CSS_SELECTOR, '.speedy-main > input')
    DEFAULT_DURATION_DROPDOWN = (By.CSS_SELECTOR, '.speedy-settings > select')