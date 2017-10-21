import re
import time

#first link to view the cruise 
base_link = 'https://www.princess.com/find/cruiseDetails.do?voyageCode=2801'

#element to find
button_element = 'md-hidden'

#gets the current time
time = time.strftime('%I:%M:%S')

forming = 'building request'
seperator = '–––––––––––––––––––––––––––––––––––––––––'

#xpath
# //*[contains(@class, 'col-pax-item selectable-blue-arrow col-xs-12 col-xs-pad-0 clearfix'), (@button, '')]
#//button[@data-num-pax="4"]/text()
#//button[@data-num-pax="4"]
# //*[contains(@class, 'col-pax-item selectable-blue-arrow col-xs-12 col-xs-pad-0 clearfix')//[contains(@button[contains(text(),'4')])]]
