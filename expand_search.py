from selenium import webdriver # boiler plate
from selenium.webdriver.chrome.service import Service # boiler plate
from selenium.webdriver.common.by import By # how I can search for something
from selenium.webdriver.common.keys import Keys # lets me do the Keys.Enter 
from selenium.webdriver.support.ui import WebDriverWait # lets us use the wait call
from selenium.webdriver.support import expected_conditions as EC # lets us use the wait call
import time

first_run = True
buttons_len = 0
def find_all_cars(driver):
    global first_run, buttons_len
    if buttons_len >= 100:
        return False

    buttons = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
    if first_run:
        buttons_len = len(buttons)
        first_run = False
    else:
        while True:
            if len(buttons) <= buttons_len:
                time.sleep(2)
                buttons = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
            else:
                buttons_len = len(buttons) 
                break
            
    driver.execute_script("arguments[0].scrollIntoView(true);", buttons[-1])

    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "hzn-button[variant='secondary'][tone='interactive']"))
    )

    for button in buttons:
        if "SEE MORE MATCHES" in button.text:
            print("BUTTON CLICK", buttons_len)
            button.click()
            return True
    
    return False

