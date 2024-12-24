from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# used to wait for page
from selenium.webdriver.support.ui import WebDriverWait
# used to get expected conditions such as presence of element
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_SPEED = 500

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


def speedTest():
    try:
        driver.get(url="https://fast.com")

        WebDriverWait(driver, 20).until(lambda driver: driver.execute_script(
            "return document.readyState") == "complete")

        speed = driver.find_element(
            By.ID, value="speed-value")
        unit = driver.find_element(
            By.ID, value="speed-units")

        bot_state = True
        while (bot_state):

            if "s" in (unit.text):
                if "speed-results-container succeeded" == speed.get_attribute("class"):
                    print(f"Your Internet speed is: {speed.text + unit.text}")
                    finalSpeed = speed.text + unit.text
                    bot_state = False
                    return f"{speed.text}-{unit.text}"

    except Exception as e:
        print(f"An error occurred: {e}")


def complain_to_Twitter(to_post):
    try:
        driver.get(url="https://x.com/i/flow/login")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text")))

        driver.find_element(
            By.NAME, value="text").send_keys(TWITTER_USERNAME, Keys.ENTER)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password")))

        driver.find_element(By.NAME, value="password").send_keys(
            TWITTER_PASSWORD, Keys.ENTER)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))

        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))

        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div').send_keys(to_post)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')))

        driver.find_element(
            By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]').click()

        print("Tweet posted successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


internetSpeed = speedTest()


if int(internetSpeed.split("-")[0]) < PROMISED_SPEED:
    post = f'''@airtelindia My Airtel wifi speeed is {
        internetSpeed} which less than my package of {PROMISED_SPEED}Mbps. Kindly fix my issue Thanks.'''
    complain_to_Twitter(post)
