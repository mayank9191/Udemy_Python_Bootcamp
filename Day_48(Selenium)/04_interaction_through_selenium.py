from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)


driver.get(url="https://www.wikipedia.org")


link = driver.find_element(By.LINK_TEXT, value="English\n6,924,000+ articles")
link.click()

# stat = driver.find_element(
#     By.XPATH, value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
# print(stat.text)

add = driver.find_element(
    By.XPATH, value='/html/body/div[1]/header/div[2]/div/a')

add.click()

name = driver.find_element(
    By.NAME, value="search")

name.send_keys("Python", Keys.ENTER)


# driver.quit()
