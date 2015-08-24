from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
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

    def test_launch_polls_site_and_check_title(self):
        # Go to check out its homepage
        self.browser.get('http://localhost:8000/polls')
        #self.browser.get('http://www.google.com')

        # Take a look at the title
        self.assertIn('This is AMAZING!!!', self.browser.title)
        #self.fail('Finish the test!')  #6
