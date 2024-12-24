from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# To send SMS
# message = client.messages.create(
#     body="Hello,Mayank 🐮!",
#     from_="+17756183366",
#     to="+919311537949",
# )

# To Send msg on Whatsapp
# message = client.messages.create(
#     from_='whatsapp:+14155238886',
#     content_sid='HX229f5a04fd0510ce1b071852155d3e75',
#     content_variables='{"1":"409173"}',
#     to='whatsapp:+919315907657'
# )

# To Make Call
# call = client.calls.create(
#     twiml="<Response><Say>Hey there its me mayank</Say></Response>",
#     from_="+17756183366",
#     to="+918700668758",
# )

# print(call.sid)
