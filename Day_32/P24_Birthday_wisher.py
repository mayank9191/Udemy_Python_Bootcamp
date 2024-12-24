from dtenv import load_dotenv
import os
from smtplib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas
import datetime as dt
import random

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

data = pandas.read_csv("Day_32/birthdays.csv")

now = dt.datetime.now()

current_year = now.year
current_month = now.month
current_date = now.day

print(dt.datetime.now().day)

for (key, value) in data.iterrows():
    if (current_date == value.day and current_month == value.month):
        random_no = random.randint(1, 3)
        age = current_year-value.year

        with open(f"Day_32/letter_templates/letter_{random_no}.txt", encoding="utf-8") as f:

            # Subject read from template that of one line (readline() only read one line)
            subject = f.readline()
            subject = subject.replace("[NAME]", value.name1).replace(
                "[AGE]", str(age))

            # Body read from template

            content = f.read()
            content = content.replace("[NAME]", value.name1).replace(
                "[AGE]", str(age))

        # To send message in proper format with emojies

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = value.email
        msg['Subject'] = subject

        msg.attach(MIMEText(content, "plain", "utf-8"))

        # Sending Email for Birthday Wish

        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email, to_addrs=value.email, msg=msg.as_string())
