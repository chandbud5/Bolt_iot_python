# IT SENDS EMAIL WHEN THERE WILL BE MORE LIGHT THAN LIMITS SET BY YOU

import email_conf as conf
from boltiot import Email, Bolt
import json, time

minimum_limit = 0 #the minimum threshold of light value 
maximum_limit = 100 #the maximum threshold of light value 


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print ("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value))
            response_text = json.loads(response.text)
            print("Response received from Mailgun is: " + str(response_text['message']))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)


#MAILGUN_API_KEY =   #'This is the private API key which you can find on your Mailgun Dashboard' 
#SANDBOX_URL=   #'You can find this on your Mailgun Dashboard' 
#SENDER_EMAIL = test@sandbox0897554323454678980
#RECIPIENT_EMAIL = 
#API_KEY = 'bolt api'
#DEVICE_ID = #'This is the ID of your Bolt device'
