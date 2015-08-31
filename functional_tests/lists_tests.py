__author__ = 'cbinder'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class LiveNewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):  #2
        #chrome_option = webdriver.ChromeOptions()
        #chrome_option.add_argument('--proxy-server=us-auto.proxy.lexmark.com:80' )
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        #self.browser.service()
        #self.browser.

    def tearDown(self):  #3
        self.browser.close()
        #self.browser.quit()

    # helper function
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        #self.browser.get('http://localhost:8000/lists')
        #self.browser.get('http://www.google.com')
        #lists_live_server_url = '{0}{1}'.format(self.live_server_url, '/lists')

        lists_live_server_url = '%s%s' % (self.live_server_url, '/lists')
        #lists_live_server_url = 'http://localhost:8000/lists'
        self.browser.get(lists_live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new To-Do list', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy peacock feathers" as an item in a
        # to-do list table
        time.sleep(2)
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists.+')
        #self.assertNotRegex(edith_list_url, '/lists.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        time.sleep(2)
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc #1
        self.browser.close()
        self.browser = webdriver.Chrome()

        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(lists_live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        time.sleep(2)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        time.sleep(2)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        time.sleep(2)

        # Satisfied, they both go back to sleep

