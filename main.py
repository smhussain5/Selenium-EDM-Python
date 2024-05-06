from selenium import webdriver
from selenium.webdriver import ChromeOptions

URL = "https://www.youtube.com/@FutureHouseMusic/videos"

driver_options = ChromeOptions()
# driver_options.add_argument("--headless=new")
driver_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=driver_options)
driver.get(URL)
driver.quit()
