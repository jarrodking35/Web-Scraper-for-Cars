from utils import *

def get_car_facts(driver):
    '''
    This method returns an array filled with car information:
    price, milage, mpg, engine/gas, drive type, transmission, color, "", "", url

    '''
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

    # this was used to try to make the webpage load faster, it is not needed unless capturing Prior Use
    # locator = (By.CSS_SELECTOR, ".overview.header.nav-target")
    # element = driver.find_element(*locator)
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Gets the rest of the car facts
    first_element = driver.find_element(By.ID, "car-page-tombstone-section")
    child_elements = first_element.find_elements(By.XPATH, "./*")
    for element in child_elements:
        text_before_newline = element.text.split('\n')[0]
        array.append(str(text_before_newline))
    
    array.append(driver.current_url)
    return array

# things to take in:
# - mpg ✔
# - drive type ✔
# - leather interior
# - accident information?
# - color ✔
# - estimated insurance?
# - estimated repair costs
# - resale value