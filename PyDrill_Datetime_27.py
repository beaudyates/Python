import datetime
import pytz

port_datetime = datetime.datetime.now(pytz.utc)

nyc_datetime = port_datetime.astimezone(pytz.timezone('US/Eastern'))
nyc_time = nyc_datetime.time()

lond_datetime = port_datetime.astimezone(pytz.timezone('Europe/London'))
lond_time = lond_datetime.time()

t_9am = datetime.time(hour=9, minute=0)
t_9pm = datetime.time(hour=9+12, minute=0)

if t_9am < nyc_time < t_9pm:
	print ("The New York office is open")
else: 
	print ("The New York office is closed")
	
if t_9am < lond_time < t_9pm:
	print ("The London office is open")
else: 
	print ("The London office is closed")
