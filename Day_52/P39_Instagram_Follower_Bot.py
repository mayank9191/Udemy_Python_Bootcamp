from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()
USER_NAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")
SEARCH = os.getenv("SEARCH")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")


driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://instagram.com")

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input'))).send_keys(USER_NAME)


WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input'))).send_keys(PASSWORD)

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button'))).click()

# WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(
#     "return document.readyState") == "complete")

# driver.get(f"https://www.instagram.com/{SEARCH}/following/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))).send_keys(SEARCH)

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/div/span'))).click()

following_count = int(WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span'))).text)

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a'))).click()


print(following_count)

for i in range(1, following_count-1):
    print(i)
    current_state = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, f'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button/div/div'))).text

    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, f'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')))

    if (current_state == "Follow"):
        button.click()
        print("Done")

    elif (current_state == "Following" or current_state == "Requested"):
        continue
    # Used To Unfollow All The Following
        # driver.implicitly_wait(10)
        # button.click()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        #     By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]'))).click()

        # print("Done")

    if (i % 5 == 0):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'))).send_keys(Keys.END)


driver.quit()
