from bs4 import BeautifulSoup  # Module used for Web Scraping
import lxml  # html parser

with open("Day_45/website.html", "r") as f:
    contents = f.read()

# Creating a object name soup which helps to parse html and scrape data
soup = BeautifulSoup(contents, "lxml")

# print the following html elements
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# formating html
# print(soup.prettify())

# To search for first anchor tag,list,paragraph etc
# print(soup.a)
# print(soup.li)
# print(soup.p)
