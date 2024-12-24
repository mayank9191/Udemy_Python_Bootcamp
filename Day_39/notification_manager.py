from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# To Send msg on Whatsapp


class Notification:
    def notification(self, msg: str, number: str):
        message = client.messages.create(
            body=msg,
            from_="+17756183366",
            to=number,
        )

        print("SMS has been sent to the user ")
