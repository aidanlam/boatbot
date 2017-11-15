from .webhooks import *
from .utils import *
from .constants import webhook
import time

def hook():
	wh = Webhook(webhook, 
		"**Boat Bot** - A room has become available! [Time: `{}`] [Bot Status: `{}`] [<!POST>]"
		.format(time.strftime('%I:%M:%S'), 
			'good')
		)
	wh.post()


