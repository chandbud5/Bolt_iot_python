# BUZZER WILL ALERT YOU WHEN BITCOIN PRICE IS MORE THAN YOUR SET SELLING PRICE (line 6)

import time,json,requests
from boltiot import Bolt

selling = 8600

# ADD YOUR API KEY AND DEVICE ID HERE
api_key = ""
device_id = ""
mybolt = Bolt(api_key,device_id)

def get_bitcoin_price():
	URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,INR,EUR" # REPLACE WITH CORRECT URL
	response = requests.request("GET", URL)
	response = json.loads(response.text)
	current_price = response["USD"]
	return current_price

while True:
#current price fetched
	current = get_bitcoin_price()
	print("Current Bitcoin price in USD is ",current)

#Check the condition
	if current>selling :
		response = mybolt.digitalWrite(0,'HIGH')
		print(response)
		time.sleep(5)
		response = mybolt.digitalWrite(0,'LOW')
		print(response)

	time.sleep(30)

# TO ADD ALERTS ON TEXT MESSAGE AND MAIL CHECKOUT mailgun_email_alert.py FILE AND message alert_twilio.py FILE.
# USING ALL THESE FILE TRY TO CREATE YOUR YOUR CODE
