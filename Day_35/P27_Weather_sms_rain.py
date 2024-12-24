from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio Account
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")
parameter = {
    "lat": "28.599406",  # MY_LATITUDE -> 28.599406
    "lon": "77.077747",  # MY_LONGITUDE -> 77.077747
    "appid": API_KEY,    # API_KEY
    "units": "metric",   # Unit in Degree Celcius
    "cnt": 4
}

# API Endpoint is of 5days/3Hrs forecast

response = requests.get(url=OWM_ENDPOINT, params=parameter)

response.raise_for_status()
data = response.json()

for i in range(4):
    weather_id = data["list"][i]["weather"][0]["id"]

    if (weather_id < 700):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It may rain today 🌧️.You must take an umbrella🌂",
            from_="+17756183366",
            to="+919315907657",
        )
        print(message.status)
        break

    else:
        print("Go my boy freely!")
        break
