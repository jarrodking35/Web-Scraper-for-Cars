from selenium import webdriver # boiler plate
from selenium.webdriver.chrome.service import Service # boiler plate
from selenium.webdriver.common.by import By # how I can search for something
from selenium.webdriver.common.keys import Keys # lets me do the Keys.Enter 
from selenium.webdriver.support.ui import WebDriverWait # lets us use the wait call
from selenium.webdriver.support import expected_conditions as EC # lets us use the wait call
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.carmax.com/cars?search=Toyota+Tacoma")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "scct--image-gallery__image"))
)

link = driver.find_element(By.CLASS_NAME, "scct--image-gallery__image")
link.click()

# most milage is 75k

time.sleep(10)
driver.quit()