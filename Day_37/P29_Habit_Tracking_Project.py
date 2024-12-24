from dotenv import load_dotenv
import os
import requests
import datetime as dt

load_dotenv()
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

# user_json = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# -------------------CREATING AN ACCOUNT WITH PIXELA------------------

# response = requests.post(url=pixela_endpoint, json=user_json)
# print(response.text)

# ---------------------CREATING(POST) OF GRAPH THROUGH PIXELA----------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "test1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ----------------------------POST PIXEL DEFINITION----------------
pixel_endpoint = f"{graph_endpoint}/test1"
today = dt.datetime(year=2024, month=2, day=1)

# pixel_config = {
#     "date": today.strftime("%Y%m%d"),  # DATE in YYYYMMDDformat
#     "quantity": "10000",
# }
# response = requests.post(
#     url=pixel_endpoint, json=pixel_config, headers=headers)

# print(response.text)

# ---------------------------PIXEL UPDATE------------------------
pixel_update_endpoint = f"{graph_endpoint}/test1/20240511"

pixel_update = {
    "quantity": "25"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)

# print(response.text)

# -----------------------------PIXEL DELETE--------------------------


delete_endpoint = f"{pixel_endpoint}/20241212"

# response = requests.delete(url=delete_endpoint, headers=headers)

# print(response.text)

# -----------------------------GET GRAPH PIXEL LIST---------------------

pixel_list_endpoint = f"{pixel_endpoint}/pixels"

# response = requests.get(url=pixel_list_endpoint, headers=headers)

# data = response.json()
# print(response.text)
# print(data)

# ------------------------DELETE MANY PIXEL----------------------------

# for i in range(1, 13):
#     for j in range(1, 32):
#         if (i == 2 and j > 29):
#             continue

#         elif (i in (4, 6, 9, 11) and j > 30):
#             continue

#         today = dt.datetime(year=2024, month=i, day=j)
#         delete_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

#         response = requests.delete(url=delete_endpoint, headers=headers)

#         print(response.text)
