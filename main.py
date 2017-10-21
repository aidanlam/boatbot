from a2.constants import *
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
from lxml import etree, html

###pkill -f firefox 
### to close all 


#page = requests.get(base_link) 
#soup = BeautifulSoup(page.content, 'html.parser')

#element = soup.find_all('button', class_=button_element)
#element = soup.find_all('button', class_=button_element)[0].get_text()



#print(element)

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

#Session info - start
print(seperator)
print('[{}] Request Made -> Status : {}'.format(time, status))

#Session info - getting info and stuff
session = start_session(base_link, button_element) #make a new session

print('[{}] Request Finished -> Token : {}'.format(time, get_token(session)))
print('[{}] Session Link -> {}'.format(time, session)) #prints the session link
# REMOVE QUITdriver.quit() #quits the current session to prevent lag


# --> now we need to see if the rooms are sold out 


status = get_status(session)
print('[{}] Using Session Link to check Stateroom Status -> {}'.format(time, status))

stateroom_xpath = '//button[@data-num-pax="4"]'
driver.find_element_by_xpath(stateroom_xpath).click()
stateroom_prices_xpath = "//section[@id='stateroom-meta']"
get_stateroom_prices = driver.find_element_by_xpath(stateroom_prices_xpath).text

#print(get_stateroom_prices)
print(etree.tostring(get_stateroom_prices, encoding='unicode', pretty_print=True))

print(seperator)

#driver.quit() Add this in later - removed for testing






