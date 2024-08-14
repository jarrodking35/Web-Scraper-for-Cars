from selenium import webdriver # boiler plate
from selenium.webdriver.chrome.service import Service # boiler plate
from selenium.webdriver.common.by import By # how I can search for something
from selenium.webdriver.common.keys import Keys # lets me do the Keys.Enter 
from selenium.webdriver.support.ui import WebDriverWait # lets us use the wait call
from selenium.webdriver.support import expected_conditions as EC # lets us use the wait call
import time

# from selenium.webdriver.chrome.options import Options

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
) # if after the specified number of SECONDS it does not find the element, crash the program

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # this will clear the content of something like a textbox
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim") # this is caps specific
# find_elements will return an array
link.click()

time.sleep(10)
driver.quit()