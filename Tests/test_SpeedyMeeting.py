import unittest
from PageObjects.Common import *
from PageObjects.Pages.LoginPage import LoginPage
from TestData.SettingsData import *
from CalendarAPI import *
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

@pytest.mark.usefixtures("driver")
class SpeedyMeetingTest(unittest.TestCase):
    def setUp(self):
        self.event_length = str(get_setting('defaultEventLength'))

    def test(self):
        loginpage = LoginPage(self.driver)
        loginpage.go_to_page(base_url())
        self.calendar_page = loginpage.login(username(), password())
        self.settings_page = self.calendar_page.go_to_settings_page(base_url() + settings_uri)
        self.settings_page.change_default_duration(self.event_length)
        self.settings_page.enable_speedy(self.event_length)
        self.settings_page.save_changes()
        self.changed_event_length = str(get_setting('defaultEventLength'))
        logger.info("Default event length now is %s" % self.changed_event_length)
        start_time, end_time = quick_add_event()
        self.settings_page.validate_default_length(start_time, end_time, self.changed_event_length)

    def tearDown(self):
        self.calendar_page.go_to_settings_page(base_url() + settings_uri)
        self.settings_page.disable_speedy(self.changed_event_length)
        self.settings_page.save_changes()


if __name__ == "__main__":
    unittest.main()
