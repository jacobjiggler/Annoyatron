from twilio.rest import TwilioRestClient
import datetime
import time
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR ACCOUNT TOKEN"
client = TwilioRestClient(account_sid, auth_token)


i = 0
tempstr = "!"
tempstr2 = "e"
endstr = " Please reply 'I hate cat facts' to stop messages "
msgcount = 0
while (i < 100) :
  tempstr = tempstr + "!"
  message = client.messages.create(body="He" + tempstr2 + "y" + tempstr + endstr,
  to="+1NUMBERTOANNOY", # Replace with your phone number
  from_="+1YOURTWILLIO NUMBER") # Replace with your Twilio number
  print message.sid
  i = i + 1
  time.sleep(300)
