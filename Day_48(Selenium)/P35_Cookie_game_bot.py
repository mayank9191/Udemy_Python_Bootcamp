from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://orteil.dashnet.org/experiments/cookie")


cookie = driver.find_element(By.XPATH, value='/html/body/div[3]/div[6]/div[9]')
money = driver.find_element(By.ID, value="money")

stop_bot = time.time() + 5*60
timeout = time.time() + 5
bot_state = True
while bot_state:
    cookie.click()
    if stop_bot >= time.time():
        if time.time() >= timeout:
            ru = [i.text.split("-") for i in driver.find_elements(
                By.CSS_SELECTOR, value="#store div b")]
            ru.pop()
            ru.reverse()
            dira = {i[0].replace(",", ""): int(
                i[1].strip().replace(",", "")) for i in ru}

            for keys in dira.keys():
                if int(money.text.replace(",", "")) > dira[keys]:
                    driver.find_element(By.ID, value=f"buy{
                                        keys.strip()}").click()
                    print("done")
                    timeout = time.time() + 5
                    break
    else:
        per_sec = driver.find_element(
            By.XPATH, value='/html/body/div[3]/div[4]/div[1]').text.split(":")[1]

        print(f"Cookies/second : {per_sec}")
        bot_state = False
