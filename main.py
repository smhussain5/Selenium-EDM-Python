"""
Responsible for scraping data from YouTube.
Information will be stored in arrays to be sent via GMail.
"""

import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

URL = "https://www.youtube.com/@FutureHouseMusic/videos"

driver_options = ChromeOptions()
driver_options.add_argument("--headless=new")
driver_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=driver_options)
driver.get(URL)

# FIND 4 LATEST
latest_button = driver.find_element(By.XPATH, "//yt-formatted-string[@title='Latest']")
latest_button.click()
time.sleep(1)
latest = driver.find_elements(
    By.XPATH, "//ytd-rich-grid-row/div[@id='contents']//a[@id='video-title-link']"
)

latest_tracks = []
latest_tracks_links = []

for track in latest[:5]:
    latest_tracks.append(track.text)
    latest_tracks_links.append(track.get_attribute("href"))

print(latest_tracks)
print(latest_tracks_links)

# FIND 4 POPULAR + LATEST
popular_button = driver.find_element(
    By.XPATH, "//yt-formatted-string[@title='Popular']"
)
popular_button.click()
time.sleep(1)
popular = driver.find_elements(
    By.XPATH, "//ytd-rich-grid-row/div[@id='contents']//a[@id='video-title-link']"
)

popular_tracks = []
popular_tracks_links = []

for track in popular[:5]:
    popular_tracks.append(track.text)
    popular_tracks_links.append(track.get_attribute("href"))

print(popular_tracks)
print(popular_tracks_links)
driver.quit()
