from dotenv import load_dotenv
import os
import datetime as dt
from smtplib import *
import random

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

now = dt.datetime.now()
week_day = now.weekday()

with open("Day_32/quotes.txt") as f:
    data = f.read()
    content = data.splitlines()
    random_word = random.choice(content)

if (week_day == 0):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, to_addrs="agrawalkrishna522@gmail.com", msg=f"Subject:Monday Motivation for you!\n\n {random_word}")
