from selenium import webdriver
import os
import htmlmin
from random import randint
import time
import yaml

def start():
	"""Runs the bot."""
	os.system('python3 bot.py')

def message(text):
	"""Sends a message in the constant format."""

	message = '[{}] {}'.format(time.strftime('%I:%M:%S'), text)
	print(message)
	
def error(location=None):
	"""Sends an error message."""

	error_msg = 'Nut! An error occurred whilst running the script.'

	if location:
		message('{} ({})'.format(error_msg, location))
	else:
		message(error_msg)

def kill():
	"""Kills all sessions to reduce lag."""

	try:
		os.system('pkill -f firefox')
	except:
		pass

def clean():
	"""Cleans and reports if an error occurred"""

	try:
		kill()
	except:
		error('Cleaning Sessions')


def config():
	"""Fetches information from the config."""

	file = 'config.yaml'

	try:
		with open(file) as r:
			data = yaml.load(r)
			
	except:
		error('Loading Config')

	

def profile():
	"""Sets up the driver profile."""

	profile = webdriver.FirefoxProfile()

	profile.set_preference("permissions.default.image", 2)
	profile.set_preference("permissions.default.stylesheet", 2)
	profile.set_preference("javascript.enabled", False)

	return profile

def webhook():
	"""Gets the webhook url."""

	data = config()
	webhook = data['webhook_url']
	return webhook

def voyage():
	"""Gets the Voyage link."""

	data = config()

	voyage = data['voyage']

	if not voyage:
		error('Missing Voyage Link in config.yaml')
	else:
		pass
		
	return voyage


def line():
	"""Prints a line."""
	line = '–––––––––––––––––––––––––––––––––––––––––'
	print(line)	
