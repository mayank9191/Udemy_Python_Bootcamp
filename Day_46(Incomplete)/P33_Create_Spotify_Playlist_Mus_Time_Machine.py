import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(
    url="https://www.billboard.com/charts/india-songs-hotw/2023-02-18/", headers=headers)

contents = response.text

#
soup = BeautifulSoup(contents, "lxml")

top_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")

song_names = soup.find_all(name="h3", id="title-of-a-story",
                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_names_list = [song.getText().strip() for song in song_names]

song_names_list.insert(0, top_song.getText().strip())
print(song_names_list)
