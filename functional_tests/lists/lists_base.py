from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        # chrome_option = webdriver.ChromeOptions()
        # chrome_option.add_argument('--proxy-server=us-auto.proxy.lexmark.com:80' )
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        # self.browser.service()
        # self.browser.

    def tearDown(self):
        self.browser.close()
        # self.browser.quit()

    # helper function
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # helper function
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
