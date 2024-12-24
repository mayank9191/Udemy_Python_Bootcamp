from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://www.linkedin.com/login")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "session_key")))
email = driver.find_element(By.NAME, value="session_key")
email.send_keys(EMAIL, Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "session_password")))
password = driver.find_element(By.NAME, value="session_password")
password.send_keys(PASSWORD, Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a')))
driver.find_element(
    By.XPATH, value='/html/body/div[6]/header/div/nav/ul/li[3]/a').click()
# driver.get(url="https://www.linkedin.com/jobs/")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')))
search = driver.find_element(
    By.XPATH, value='/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]').send_keys("python developer", Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button')))
easy_apply = driver.find_element(
    By.XPATH, value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button').click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input')))
phone_no = driver.find_element(
    By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input').send_keys("9315907657", Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')))
next = driver.find_element(
    By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span").click()

next = driver.find_element(
    By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span").click()
