from core import *
from bot import *
import sys

config = config()
voyage = config['voyage']
guests = config['guests']

if not voyage and guests:
	error('Missing Config Values')	
	print('Please fill out the config.yaml')
else:
	try:
		message('Starting Boat Bot!')
		start()
	except:
		error('Starting Bot')
