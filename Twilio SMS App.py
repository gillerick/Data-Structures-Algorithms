
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="If you received this message, then Twilio SMS Alerts is all good. :)",
    from_='+15672293660',
    to='+14087075185'
)

print(message.sid)
