from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="",
    to="",    # Replace with your phone number
    from_="") # Replace with your Twilio number
print message.sid
