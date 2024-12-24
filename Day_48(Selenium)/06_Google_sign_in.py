from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(
    "--disable-blink-features=AutomationControlled")  # Hide automation flag
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Launch WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://accounts.google.com/signin")


email = driver.find_element(By.NAME, value="identifier")
time.sleep(3)
email.send_keys("rohankumar94942@gmail.com", Keys.ENTER)
time.sleep(3)
lname = driver.find_element(By.NAME, value="Passwd")
time.sleep(3)
lname.send_keys("Kulahara@1234", Keys.ENTER)

time.sleep(3)
