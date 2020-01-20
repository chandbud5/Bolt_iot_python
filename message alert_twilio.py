# THIS WILL GIVE YOU ALERT ON YOUR MOBILE THROUGH TEXT MESSAGE WHEN TEMP. IS OUTSIDE YOUR THRESHOLD LIMIT

import twconfig, json, time
from boltiot import Sms, Bolt
minimum_limit = 0
maximum_limit = 50
mybolt = Bolt(twconfig.API_KEY, twconfig.DEVICE_ID)
sms = Sms(twconfig.SID, twconfig.AUTH_TOKEN, twconfig.TO_NUMBER, twconfig.FROM_NUMBER)
while True:
	print("Reading Sensor Value")
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print("sensor value is : "+str(data['value']))
	try:
		sensor_value = int(data['value'])
		if sensor_value > maximum_limit or sensor_value < minimum_limit:
			print("Making request to Twilio to send SMS")
			response = sms.send_sms("The current temperature sensor value is "+str(sensor_value))
			print("Response recieved from Twilio is "+ str(response))
			print("Status of SMS at Twilio is "+str(response.status))
	except Exception as e:
		print("Error occured: Below are details")
		print(e)
	time.sleep(10) 


#SID = 
#AUTH_TOKEN = 
#FROM_NUMBER = twilio number
#TO_NUMBER = your
#API_KEY = bolt
#DEVICE_ID = bolt
