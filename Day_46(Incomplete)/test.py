from dotenv import load_dotenv
import os
import requests

load_dotenv()
ClientID = os.getenv("SPOTIFY_CLIENT_ID")
ClientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")


def getToken():
    token_url = "https://accounts.spotify.com/api/token"

    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    input = {
        "grant_type": "client_credentials",
        "client_id": ClientID,
        "client_secret": ClientSecret
    }

    response = requests.post(url=token_url, headers=header, data=input)

    return response.json()["access_token"]


headers = {
    "Authorization": "Bearer " + getToken(),
    "scopes": "playlist-modify-private"
}

# parameter = {
# }
response = requests.put(
    url="https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg", headers=headers)

# print(headers)
print(response)
