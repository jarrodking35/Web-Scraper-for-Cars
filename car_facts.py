from selenium import webdriver # boiler plate
from selenium.webdriver.chrome.service import Service # boiler plate
from selenium.webdriver.common.by import By # how I can search for something
from selenium.webdriver.common.keys import Keys # lets me do the Keys.Enter 
from selenium.webdriver.support.ui import WebDriverWait # lets us use the wait call
from selenium.webdriver.support import expected_conditions as EC # lets us use the wait call

def get_car_facts(driver):
    array = []
    # get the price of the car and the mileage
    WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "default-price-display"))
            )
    price = driver.find_element(By.ID, "default-price-display")
    array.append(price.text)

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.car-header-mileage"))
    )
    mileage = driver.find_element(By.CSS_SELECTOR, "span.car-header-mileage")
    array.append(mileage.text)


    # locator = (By.CSS_SELECTOR, ".overview.header.nav-target")
    # element = driver.find_element(*locator)
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)

    first_element = driver.find_element(By.ID, "car-page-tombstone-section")
    child_elements = first_element.find_elements(By.XPATH, "./*")
    for element in child_elements:
        text_before_newline = element.text.split('\n')[0]
        array.append(str(text_before_newline))
    
    array.append(driver.current_url)
    return array

# array should look like: price, milage, mpg, engine/gas, drive type, transmission, color, "", ""



# things to take in:
# - mpg ✔
# - drive type ✔
# - leather interior
# - accident information?
# - color ✔
# - estimated insurance?
# - estimated repair costs
# - resale value