from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Path to your Chrome profile (replace with your actual profile path)
chrome_profile_path = r"C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data"

# Configure Chrome options
options = Options()


options.add_argument(f"user-data-dir={chrome_profile_path}")
# Replace "Default" with your profile name if different
options.add_argument("profile-directory=Rohan")

# Start Chrome with the specified profile
driver = webdriver.Chrome(service=Service(
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"), options=options)
