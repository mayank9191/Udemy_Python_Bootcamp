import requests
from bs4 import BeautifulSoup
import lxml


response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

content = response.text

soup = BeautifulSoup(content, "lxml")


movie_names = soup.find_all(name="h3", class_="title")
movie_names.reverse()

for movie in movie_names:
    with open("Day_45/movies.txt", "a", encoding="utf-8") as f:
        f.write(movie.getText() + "\n")
