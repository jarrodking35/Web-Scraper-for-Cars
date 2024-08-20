from selenium import webdriver # boiler plate
from selenium.webdriver.chrome.service import Service # boiler plate
from selenium.webdriver.common.by import By # how I can search for something
from selenium.webdriver.common.keys import Keys # lets me do the Keys.Enter 
from selenium.webdriver.support.ui import WebDriverWait # lets us use the wait call
from selenium.webdriver.support import expected_conditions as EC # lets us use the wait call
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.carmax.com/cars/toyota/tacoma")

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Distance & Shipping']"))
# )


# button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Distance & Shipping']")
# button.click()

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "distance--change-store-link--YvAJJ"))
# )

# button = driver.find_element(By.CLASS_NAME, "distance--change-store-link--YvAJJ")
# button.click()


# WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "store-chooser-keyword-input"))
# )

# input_element = driver.find_element(By.ID, "store-chooser-keyword-input")
# input_element.clear() # this will clear the content of something like a textbox
# WebDriverWait(driver, 40).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='set store']"))
# )
# input_element.send_keys("17601" + Keys.ENTER)

# WebDriverWait(driver, 40).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='set store']"))
# )

# button = driver.find_element(By.CSS_SELECTOR, "[aria-label='set store']")
# button.click()

# while True:
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Distance & Shipping']"))
#         )

#         # Click the next button
#         button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Distance & Shipping']")
#         button.click()
#         break
#     except Exception as e:
#         time.sleep(4)

# WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "distanceSelect"))
#         )
# element = driver.find_element(By.ID, "distanceSelect")
# driver.execute_script("arguments[0].setAttribute('value', '75')", element)
# driver.execute_script("var event = new Event('change', { bubbles: true }); arguments[0].dispatchEvent(event);", element)

WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scct--image-gallery__image"))
        )

buttons = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
for index in range(len(buttons)):
    try:
        # Re-find the elements in case the page has changed
        elements = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
        element = elements[index]

        # Perform actions on each element - in this case, click on a car
        element.click()

        # -----------------------------------------------
        # GET ALL THE INFORMATION I WANT FROM A CARS PAGE












        



        # -----------------------------------------------

        # Optionally, wait for the page to load or perform other actions
        time.sleep(2)  # Add a delay if necessary
        driver.back()  # Go back to the previous page, if needed

    except Exception as e:
        print(f"Element at index {index} became stale.")
        continue  # Skip to the next iteration

# most milage is 75k
time.sleep(100)
driver.quit()


'''
Here is what I need to do:
   - I need to have selenium start at a certain car location, and search in a 100 mile radius (DONE)
   - I need selenium to gather data on each car
      -- I need to first print all the information im going to use to the console
   - I want to export this data into a csv file
   - Then I can think about sorting the data, maybe some data analytics stuff available here
'''