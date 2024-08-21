from utils import *

def set_distance(driver):
    '''
    This method sets the distance away you would like to search through
    '''
    # set the distance, doing it like this waits for the new page to load
    while True:
        try:
            WebDriverWait(driver, 100).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Distance or Shipping']"))
            )

            # Click the next button
            button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Distance or Shipping']")
            button.click()
            break
        except Exception as e:
            time.sleep(4)

    # set the distance
    WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "distanceSelect"))
            )
    element = driver.find_element(By.ID, "distanceSelect")
    driver.execute_script("arguments[0].setAttribute('value', '100')", element)
    driver.execute_script("var event = new Event('change', { bubbles: true }); arguments[0].dispatchEvent(event);", element)
