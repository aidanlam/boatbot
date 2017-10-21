from a2.constants import *
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
import html
import htmlmin
import time
from random import randint
import logging

wait = randint(10, 15)

start()
	
driver = webdriver.Firefox() #Start a new driver session

def start_session(link, element):
	"""Creates a new stateroom session."""
	try:
		driver.get(link) #Goto the webpage
		driver.find_element_by_class_name(element).click() #Find the element and click on it 'md-hidden'
		session = driver.current_url #get the new session link
	except:
		driver.quit() 
		session = 'error'

	return session

def get_token(link):
	"""Gets the session token."""

	token = link.rsplit('sessionToken=', 1)[-1]
	return token

def get_status(link):
	"""Gets the page status."""
	page = requests.get(link)
	status = page.status_code

	return status

status = get_status(base_link)


print(seperator)
print('[{}] Request Made -> Status : {}'.format(get_time, status))
session = start_session(base_link, button_element)
print('[{}] Request Finished -> Token : {}'.format(get_time, get_token(session)))
print('[{}] Session Link -> {}'.format(get_time, session)) 


# --> now we need to see if the rooms are sold out 


status = get_status(session)
print('[{}] Using Session Link to check Stateroom Status -> {}'.format(get_time, get_token(session)))

stateroom_xpath = '//button[@data-num-pax="4"]'
driver.find_element_by_xpath(stateroom_xpath).click()

#We need to wait for the element to load or else we get 
#../what_happends_when_we_dont_await.html
stateroom_prices_xpath = "//section[@id='stateroom-meta']"

#update 7s isnt enough
print('[{}] Waiting for ({}) to load. -> About : -{}s'.format(get_time, stateroom_prices_xpath, wait))
time.sleep(wait) #Wait for 15 sescons


element = driver.find_element_by_xpath(stateroom_prices_xpath).get_attribute('innerHTML')
compressing_status = 'Working'
print('[{}] Compressing HTML -> Working [{}]'.format(get_time, compressing_status))
global stateroom_element
try:
	stateroom_element = htmlmin.minify(element, remove_empty_space=True)
	compressing_status = 'Done'
	print('[{}] Compressing HTML -> Working [{}]'.format(get_time, compressing_status))
except:
	stateroom_element = element
	compressing_status = 'Error'
	print('[{}] Compressing HTML -> Working [{}]'.format(get_time, compressing_status))


time.sleep(2)
print('[{}] Stateroom Price Data Found -> Analyzing Data'.format(get_time))

#USED FOR TEST
#stateroom_element = 'Sold Out Sold Out Sold Out Sold Out Sol'

if stateroom_element.count(sold_out) == 5:
	print('[{}] Analyzing Data is Finished -> Rooms are still sould out.'.format(get_time))
	#restart the timer
else:
	print('[{}] Analyzing Data is Finished -> Rooms Open'.format(get_time))
	print('[{}] Sending notificiation -> Working'.format(get_time))

		#now we try to send the notificiation

		#restart the timer even tho the room is open cuz we want to know about the room!

print(seperator)
driver.close()
