from PageObjects.Locators.CalendarPageLocators import CalendarPageLocators
from time import sleep
from BasePage import BasePage
from SettingsPage import SettingsPage


class CalendarPage(BasePage):
    def go_to_settings_page(self, url):
        self.go_to(url)
        return SettingsPage(self.driver)

    def assert_timings(self, format):
        elements = self.findall(CalendarPageLocators.CALENDAR_TIMINGS)
        for element in elements:
            time = element.text
            if format == "24":
                assert "am" not in time.lower(), 'time is not in 24hr format'
                assert "pm " not in time.lower(), 'time is not in 24hr format'
            else:
                is_12hr = False
                if "am" in time.lower() or "pm" in time.lower():
                    is_12hr = True
                assert is_12hr, 'time is not in 12hr format'

    def assert_weekstart(self, changed_weekstart):
        element = self.find(CalendarPageLocators.FIRST_WEEKDAY)
        weekday = element.text
        assert changed_weekstart in weekday
