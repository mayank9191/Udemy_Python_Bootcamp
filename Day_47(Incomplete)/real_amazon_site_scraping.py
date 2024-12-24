# To Handel the real site we need to use the proxies or VPN or chapcha solver

import requests
from bs4 import BeautifulSoup
import lxml


headers = {
    "Accept-Language": "en-US,en",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",

}

proxies = {"http": "http://186.237.131.122:8080",
           "https": "http://43.224.116.125:8080"}

response = requests.get(
    url="https://www.amazon.in/Samsung-Galaxy-Ultra-Phantom-Storage/dp/B0BT9FDZ8N/ref=bmx_dp_jihi0cin_d_sccl_2_2/262-0730454-7095311", headers=headers, proxies=proxies)

contents = response.text

soup = BeautifulSoup(contents, "lxml")

with open("Day_47/index.html", "w") as f:
    f.write(str(soup))
    print("done")
