from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from io import StringIO
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("FB_EMAIL")
pw = os.getenv("FB_PW")

browser = webdriver.Chrome()
browser.get('https://facebook.com')

elem = browser.find_element_by_id('email')
elem.send_keys(email)
elem = browser.find_element_by_id('pass')
elem.send_keys(pw)

button = browser.find_element_by_id('loginbutton').click()
