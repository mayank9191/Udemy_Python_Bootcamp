# TO add chech in date and check out date(table logic) and add it to the form
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

chrome_options = webdriver.ChromeOptions()


chrome_options.add_argument("--enable-automation")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

name_list = []
price_list = []
link_list = []


def get_data_from_airbnb(city):

    driver.get("https://www.airbnb.co.in/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[1]/div[1]/label/div/input'))).send_keys(city, Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/button[3]'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/button'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[2]/div[1]'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div/div/div/div[1]/div[2]/button[2]'))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[2]/div[3]/button'))).click()

    driver.implicitly_wait(10)
    for i in range(1, 19):
        driver.implicitly_wait(10)
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{i}]/div/div[2]/div/div/div/div/div/div[2]/div[2]/span')))

        no = math.ceil(len(driver.find_elements(By.XPATH, f'/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{
            i}]/div/div[2]/div/div/div/div/div/div[2]/div[5]/div[2]/div/div/span/div/span'))/2)

        price = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{i}]/div/div[2]/div/div/div/div/div/div[2]/div[5]/div[2]/div/div/span/div/span[{no}]'))).text

        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{i}]/div/div[2]/div/div/div/div/a'))).get_attribute("href")

        price_list.append(price)
        name_list.append(name.text)
        link_list.append(link)


def fill_form(name_list, price_list, link_list):
    driver.get(url="https://forms.gle/Gq8mR1QproFoE79x8")

    for i in range(0, len(name_list)):
        driver.implicitly_wait(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea'))).send_keys(name_list[i])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea'))).send_keys(price_list[i])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'))).send_keys(link_list[i])

        driver.find_element(
            By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()

        time.sleep(2)
        driver.get(url="https://forms.gle/Gq8mR1QproFoE79x8")
    print("Done")


get_data_from_airbnb("Goa")
fill_form(name_list=name_list, price_list=price_list, link_list=link_list)
driver.quit()

# Date table logic

# /html/body/div[5]/div/div/div[1]/div/div[3]/header/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/div/div
# /html/body/div[5]/div/div/div[1]/div/div[3]/header/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]/div/div
# /html/body/div[5]/div/div/div[1]/div/div[3]/header/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/div/div
# /html/body/div[5]/div/div/div[1]/div/div[3]/header/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[6]/div/div
