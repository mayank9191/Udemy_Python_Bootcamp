from dotenv import load_dotenv
import os
import requests
import html
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_parameter = {
    "qinTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
# response.raise_for_status()

# data = response.json()["Time Series (Daily)"]

# data_list = [value for (key, value) in data.items()]

# yesterday_close_price = float(data_list[0]["4. close"])
# day_before_yesterday_close_price = float(data_list[1]["4. close"])

# # For Absolute value

# difference = abs(yesterday_close_price - day_before_yesterday_close_price)

# if ((difference/yesterday_close_price)*100 >= 5):
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="Hello,Mayank 🐮!",
#         from_="+17756183366",
#         to="+99315907657",
#     )

# else:
#     print((difference/yesterday_close_price)*100)

response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
response.raise_for_status()

articles = response.json()["articles"]
three_articles = articles[:3]

format_articles_list = [f"Headline:{html.unescape(
    i["title"])}" + "\n" + f"Brief:{html.unescape(i["description"])}" for i in three_articles]


client = Client(account_sid, auth_token)
message = client.messages.create(
    body=format_articles_list,
    from_="+17756183366",
    to="+919315907657",
)

print(message.sid)
