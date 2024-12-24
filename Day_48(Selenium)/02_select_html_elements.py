from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://youtube.com")


# string = driver.find_element(
#     By.CLASS_NAME, value="title.style-scope.ytd-mini-guide-entry-renderer")

# search_bar = driver.find_element(By.NAME, value="search_query")
# print(f"{string.tag_name}")

# print(search_bar.get_attribute("placeholder"))

# subs = driver.find_element(
#     By.CLASS_NAME, value="yt-core-attributed-string.yt-content-metadata-view-model-wiz__metadata-text.yt-core-attributed-string--white-space-pre-wrap.yt-core-attributed-string--link-inherit-color")

# print(subs.text)

# subs_button = driver.find_element(
#     By.CLASS_NAME, value="yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m")

# print(subs_button.size)

# yt_image = driver.find_element(
#     By.CLASS_NAME, value="yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded")

# print(yt_image.get_attribute("src"))


# yt_image = driver.find_element(
#     By.CLASS_NAME, value="yt-core-image.yt-spec-avatar-shape__image.yt-core-image--fill-parent-height.yt-core-image--fill-parent-width.yt-core-image--content-mode-scale-to-fill.yt-core-image--loaded")
# link = yt_image.get_attribute("src")

# css = driver.find_element(
#     By.CSS_SELECTOR, value=".ytSearchboxComponentSearchForm input")
# print(css.get_attribute("placeholder"))

# xPath = driver.find_element(
#     By.XPATH, value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-section-renderer/div/ytd-feed-nudge-renderer/div[1]/div[2]/div[2]/div[2]/yt-formatted-string')

# print(xPath.text)

# contents = driver.find_elements()

# print(contents)

driver.quit()
