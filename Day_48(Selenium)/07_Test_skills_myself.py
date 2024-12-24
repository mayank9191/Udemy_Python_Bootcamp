from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://tinder.com/")

time.sleep(3)
accept = driver.find_element(
    By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
time.sleep(3)
accept.click()

create = driver.find_element(
    By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/div[3]/div/div[2]/button/div[2]/div[2]/div')
time.sleep(3)
create.click()
time.sleep(3)
google = driver.find_element(
    By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div/div/div/div/iframe')
google.click()
time.sleep(4)
email = driver.find_element(
    By.XPATH, value='/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div')
email.send_keys("roohitaneja49@gmail.com", Keys.ENTER)
time.sleep(3)
