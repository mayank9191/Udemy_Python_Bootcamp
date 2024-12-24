from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
ClientID = os.getenv("SPOTIFY_CLIENT_ID")
ClientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ClientID,
                                               client_secret=ClientSecret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"
                                               ))

results = sp.user_playlist_create(
    user="31q7jfod5wzgvx7wsqwk7gkja6la", name="Test-01")

# print(results["item"]["name"])
# print(results["items"])
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
