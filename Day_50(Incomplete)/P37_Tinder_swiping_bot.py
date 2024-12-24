from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "--disable-blink-features=AutomationControlled")  # Hide automation flag
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Launch WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get(url="https://tinder.com/")

# Click on Login button
WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')))
time.sleep(2)
driver.find_element(
    By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]').click()

# click to Continue with google
WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div/div/div/div')))
time.sleep(2)
driver.find_element(
    By.XPATH, value='/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div/div/div/div').click()


# Get the current window handle (main window)
main_window = driver.current_window_handle

# Wait for the new window to open and switch to it
WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

# Select google login window and Returns the handles of all windows within the current session.
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "identifier")))
time.sleep(2)
driver.find_element(By.NAME, value="identifier").send_keys(
    EMAIL, Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "Passwd")))
time.sleep(2)
driver.find_element(By.NAME, value="Passwd").send_keys(
    PASSWORD, Keys.ENTER)

time.sleep(2)
driver.switch_to.window(main_window)

driver.get(url="https://tinder.com/app/explore")

time.sleep(11)
