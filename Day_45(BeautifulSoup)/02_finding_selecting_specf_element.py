from bs4 import BeautifulSoup
import lxml

with open("Day_45/website.html", "r") as f:
    contents = f.read()


soup = BeautifulSoup(contents, "lxml")

# To get all specified tag
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href")) # get attribute
    pass

# Find -> Returns first page element
# Find_all -> Returns all page element

# if there are many tags of same name we can find specific by(id,class_)
heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

# To get particular tag by specifying selector
name = soup.select_one(selector="#name")  # select_one give first item
print(name)


headings = soup.select(selector=".heading")  # select give me all match item
print(headings.getText())
