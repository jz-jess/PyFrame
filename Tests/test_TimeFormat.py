import unittest
from PageObjects.Common import *
from PageObjects.Pages.LoginPage import LoginPage
from TestData.SettingsData import *
from CalendarAPI import *


@pytest.mark.usefixtures("driver")
class TimeFormatTest(unittest.TestCase):
    def setUp(self):
        self.is_24hr = str(get_setting('format24HourTime'))

    def test(self):
        loginpage = LoginPage(self.driver)
        loginpage.go_to_page(base_url())
        calendar_page = loginpage.login(username(), password())
        settings_page = calendar_page.go_to_settings_page(base_url() + settings_uri)
        format = settings_page.change_time_format(self.is_24hr)
        settings_page.save_changes()
        calendar_page.assert_timings(format)


if __name__ == "__main__":
    unittest.main()
