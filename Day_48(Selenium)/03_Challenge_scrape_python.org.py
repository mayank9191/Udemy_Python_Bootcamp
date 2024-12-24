from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://www.python.org")

menu = driver.find_elements(
    By.XPATH, value='/html/body/div[1]/div[3]/div/section/div[3]/div[2]/div/ul/li')

x = ""
for i in range(len(menu)):
    x += menu[i].text + "\n"

event_list = x.split("\n")

dict = {}
for i in range(0, len(event_list)-1, 2):
    dict[int((i/2))] = {"time": event_list[i], "name": event_list[i+1]}

print(dict)
driver.quit()
