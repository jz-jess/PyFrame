import unittest
from PageObjects.Common import *
from PageObjects.Pages.LoginPage import LoginPage
from TestData.SettingsData import *
from CalendarAPI import *


class WeekChangeTest(unittest.TestCase):
    def setUp(self):
        self.driver = open_browser()
        self.week_start = str(get_setting('weekStart'))

    def test(self):
        loginpage = LoginPage(self.driver)
        loginpage.go_to_page(base_url())
        calendar_page = loginpage.login(username(), password())
        settings_page = calendar_page.go_to_settings_page(base_url() + settings_uri)
        changed_weekstart = settings_page.change_weekstart(self.week_start)
        settings_page.save_changes()
        calendar_page.assert_weekstart(changed_weekstart)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
