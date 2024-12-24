from dotenv import load_dotenv
import os
import requests
import datetime as dt
from smtplib import *
import time

MY_LAT = 28.599406
MY_LNG = 77.077747


email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# ISS API

# Response code to show status of our request Eg:
# 1XX: Hold On (Wait for some time)
# 2XX: Here You Go (Successful)
# 3XX: Go Away (not have Permission)
# 4XX: You Screwed Up
# 5XX: I Screwed Up (server side issue)


paramerters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
    # "tzid": "Asia/Kolkata"
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5):
        return True


def is_night():
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=paramerters)

    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now_hour = dt.datetime.now().hour

    if (sunset <= now_hour or now_hour <= sunrise):
        return True


while True:
    time.sleep(60)
    if (is_iss_overhead() and is_night()):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg='''Subject:Look Up now from terrace! The ISS is Overhead \n\nQuick heads-up! The International Space Station is right above you in the sky right now.''')
