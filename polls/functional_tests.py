__author__ = 'cbinder'

from selenium import webdriver
# import selenium.webdriver.chrome.service as service

# service = service.Service('/usr/local/bin/chromedriver')
# service.start()
# capabilities = {'chrome.binary' : ''}
browser = webdriver.Chrome()
#browser.get('http://www.google.com')
browser.get('http://localhost:8000/polls')

assert 'This is AMAZING!!!' in browser.title