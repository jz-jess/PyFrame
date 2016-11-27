from PageObjects.Locators.SettingsPageLocators import SettingsPageLocators
from time import sleep
from BasePage import BasePage
import CalendarPage
import datetime


class SettingsPage(BasePage):
    def go_to_calendar_page(self):
        self.click_element(SettingsPageLocators.CALENDARPAGE_LINK)
        return CalendarPage.CalendarPage(self.driver)

    def change_time_format(self, is_24):
        if is_24 == 'false':
            self.select_dropdown_by_visible_text(SettingsPageLocators.TIME_FORMAT_DRODPDOWN, '13:00')
            return '24'
        else:
            self.select_dropdown_by_visible_text(SettingsPageLocators.TIME_FORMAT_DRODPDOWN, '1:00pm')
            return '12'

    def save_changes(self):
        self.click_element(SettingsPageLocators.SAVE_BUTTON)
        return CalendarPage.CalendarPage(self.driver)

    def change_weekstart(self, week_start):
        if week_start == '0':
            self.select_dropdown_by_value(SettingsPageLocators.WEEK_START_DROPDOWN, '1')
            weekstart = 'Mon'
        elif week_start == '1':
            self.select_dropdown_by_value(SettingsPageLocators.WEEK_START_DROPDOWN, '6')
            weekstart = 'Sat'
        else:
            self.select_dropdown_by_value(SettingsPageLocators.WEEK_START_DROPDOWN, '0')
            weekstart = 'Sun'
        return weekstart

    def enable_speedy(self, event_length):
        speedy_times = ['25', '50', '80', '110']
        if event_length not in speedy_times:
            self.click_element(SettingsPageLocators.SPEEDY_MEETING_CHECKBOX)

    def disable_speedy(self, event_length):
        speedy_times = ['25', '50', '80', '110']
        if event_length in speedy_times:
            self.click_element(SettingsPageLocators.SPEEDY_MEETING_CHECKBOX)

    def validate_default_length(self, start_time, end_time, event_length):
        fmt = '%H:%M'
        d1 = datetime.datetime.strptime(start_time, fmt)
        d2 = datetime.datetime.strptime(end_time, fmt)
        diff = str(d2-d1)
        h,m,s = diff.split(':')
        h = int(h)
        m = int(m)
        diff_minutes = h * 60 + m
        assert diff_minutes == int(event_length)

    def change_default_duration(self, event_length):
        if event_length == '60' or event_length == '50':
            self.select_dropdown_by_value(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '90')

        elif event_length == '15':
            self.select_dropdown_by_value(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '30')

        elif event_length == '30' or event_length == '25':
            if event_length == '25':
                self.select_dropdown_by_visible_text(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '50 minutes')
            else:
                self.select_dropdown_by_visible_text(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '60 minutes')

        elif event_length == '90' or event_length == '80':
            self.select_dropdown_by_value(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '120')

        else:
            self.select_dropdown_by_value(SettingsPageLocators.DEFAULT_DURATION_DROPDOWN, '30')
