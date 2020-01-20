import time,json,requests
from boltiot import Bolt

selling = 8575

api_key = "57844883-03f3-4621-a0c1-d7c2a494fedf"
device_id = "BOLT290817"
mybolt = Bolt(api_key,device_id)

def get_bitcoin_price():
	URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,INR,EUR" # REPLACE WITH CORRECT URL
	response = requests.request("GET", URL)
	response = json.loads(response.text)
	current_price = response["USD"]
	return current_price

while True:
#current price fetched
#	data = mybolt.isOnline()
#	print("Device status by isOnline  ",data)

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
