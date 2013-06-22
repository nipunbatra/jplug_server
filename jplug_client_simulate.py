'''This program simulates a JPlug client and sends a request fo given number of jplugs
to a particular IP address'''

#TO make HTTP requests
import requests

#To sleep and emulate sampling at fixed interval
import time

#To create dummy random data
import random


#Localhost IP for testing
SERVER_IP_ADDRESS="http://127.0.0.1:9000/jplug"

#Create some dummy MAC addresses
JPLUG_MACS=["001E1E1E0"+str(x) for x in range(10)]

#Upload interval in s
UPLOAD_INTERVAL=1

'''Create random set of values for a jplug reading
	Format (Can easily modify to add/remove parameters)
	mac,timestamp(epoch),voltage,frequency,active_power,reactive_power,energy
	'''
def create_random_datapoint(jplug_mac):
	return jplug_mac+","+str(int(time.time()))+","+str(random.randint(230,240))+","+str(random.randint(49,52))+","+str(random.randint(0,400))+","+str(random.randint(0,400))+",\n"
	
while True:
	try:
		for jplug_mac in JPLUG_MACS:
			#Make a post request
			data_packet=create_random_datapoint(jplug_mac)
			req=requests.post(SERVER_IP_ADDRESS,data_packet)
		time.sleep(UPLOAD_INTERVAL)
	except Exception,e:
		print e
		time.sleep(UPLOAD_INTERVAL)
		continue
