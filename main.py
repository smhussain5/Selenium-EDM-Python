from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

URL = "https://www.youtube.com/@FutureHouseMusic/videos"

driver_options = ChromeOptions()
driver_options.add_argument("--headless=new")
driver_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=driver_options)
driver.get(URL)

# TODO: FIND 4 LATEST
latest_button = driver.find_element(By.XPATH, "//yt-formatted-string[@title='Latest']")
latest_button.click()
latest_tracks = driver.find_elements(
    By.XPATH, "//ytd-rich-grid-row/div[@id='contents']//a[@id='video-title-link']"
)

for track in latest_tracks[:5]:
    print(track.text)
    print(track.get_attribute("href"))

# TODO: FIND 4 POPULAR + LATEST
popular_button = driver.find_element(
    By.XPATH, "//yt-formatted-string[@title='Popular']"
)
popular_button.click()
popular_tracks = driver.find_elements(
    By.XPATH, "//ytd-rich-grid-row/div[@id='contents']//a[@id='video-title-link']"
)

for track in popular_tracks[:5]:
    print(track.text)
    print(track.get_attribute("href"))

driver.quit()
