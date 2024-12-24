import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get(url="https://news.ycombinator.com/news")

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

article_text = []
article_link = []
article_upvotes = []
articles = soup.find_all(name="span", class_="titleline")

for article_tag in articles:
    article_text.append(article_tag.a.getText())
    article_link.append(article_tag.a.get("href"))


article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(
    name="span", class_="score")]

# print(article_text)
# print(article_link)
# print(article_upvotes)

largest_upvotes = max(article_upvotes)

index = article_upvotes.index(largest_upvotes)
print(largest_upvotes)
print(article_text[index+1])
print(article_link[index+1])
