from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

myTwilioNumber = os.environ['MY_TWILIO_NUMBER']
myCellPhone = os.environ['MY_CELL_PHONE_NUMBER']

message = client.messages.create(body="testing env",from_=myTwilioNumber,to=myCellPhone)  
print(message.sid)
