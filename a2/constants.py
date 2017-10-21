import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
import html
import htmlmin
import time

def start():
	"""Clears and starts everything """
	os.popen('pkill -f firefox')
	time.sleep(2)

#first link to view the cruise 
base_link = 'https://www.princess.com/find/cruiseDetails.do?voyageCode=2801'

#element to find
button_element = 'md-hidden'

#gets the current time
get_time = time.strftime('%I:%M:%S')

forming = 'building request'
seperator = '–––––––––––––––––––––––––––––––––––––––––'

#xpath
# //*[contains(@class, 'col-pax-item selectable-blue-arrow col-xs-12 col-xs-pad-0 clearfix'), (@button, '')]
#//button[@data-num-pax="4"]/text()
#//button[@data-num-pax="4"]
# //*[contains(@class, 'col-pax-item selectable-blue-arrow col-xs-12 col-xs-pad-0 clearfix')//[contains(@button[contains(text(),'4')])]]


######Values to search for
interior = 'Interior from'
oceanview = 'Oceanview from'
balcony = 'Balcony from'
minisuite = 'Mini-Suite from'
suite = 'Suite frome'
sold_out = 'Sold Out'
#

test_html = """Sold Out"""
