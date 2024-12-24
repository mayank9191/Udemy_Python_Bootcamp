from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

response = requests.get(url="https://appbrewery.github.io/instant_pot")

content = response.text

soup = BeautifulSoup(content, "lxml")


product = " ".join(soup.find(name="span", id="productTitle",
                             class_="a-size-large product-title-word-break").getText().split(" ")[1:5])

price = float(soup.find(name="span", class_="a-price-whole").getText() +
              soup.find(name="span", class_="a-price-fraction").getText())

print(price)
if (price < 100):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = "Amazon Price Alert!"

        msg.attach(MIMEText(f"{product} is now ${price}", "plain", "utf-8"))
        connection.sendmail(
            from_addr=email, to_addrs=email, msg=msg.as_string())
    print("sent")
