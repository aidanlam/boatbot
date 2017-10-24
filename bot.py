from core import *
from selenium import webdriver
import re
import sys


clean()
config = config()

profile = profile()
driver = webdriver.Firefox(firefox_profile=profile)

voyage_link = config['voyage']
driver.get(voyage_link) #Visits the landing page

voyage_info = driver.find_element_by_class_name('md-hidden') #Finds the Select Room button
voyage_info.click()

session_link = driver.current_url

message(session_link)

guests = config['guests']
guests_validator = re.match('^[-+]?[0-4]+$', guests)

if not guests_validator:
	error('Guests is not [1-4]')
	sys.exit()
else:
	stateroom_xpath = '//button[@data-num-pax="{}"]'.format(guests)

driver.find_element_by_xpath(stateroom_xpath).click()
time.sleep(5)

element = driver.find_element_by_xpath('//section[@id="stateroom-meta"]').get_attribute('innerHTML')
stateroom_element = htmlmin.minify(element, remove_empty_space=True)

if stateroom_element.count('Sold Out') == 5:
	message('Analyzing Data Finished -> All Rooms Sold Out')
else:
	message('Analyzing Data Finished -> A Room is Available')
	#TODO Notify








