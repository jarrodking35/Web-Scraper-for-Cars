from utils import *
from car_facts import get_car_facts
from expand_search import find_all_cars

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.carmax.com/cars/toyota/tacoma")

# check that I can click the button Distance or Shipping
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Distance or Shipping']"))
)
# click the button Distance or Shipping
button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Distance or Shipping']")
button.click()

# check that I can click the button change store
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "store-info--change-store-link--Etcao"))
)
# click the button change store
button = driver.find_element(By.CLASS_NAME, "store-info--change-store-link--Etcao")
button.click()

# check that I can click the input text box
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "store-chooser-keyword-input"))
)
# click the textbox and set it
input_element = driver.find_element(By.ID, "store-chooser-keyword-input")
input_element.clear() # this will clear the content of something like a textbox
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='set store']"))
)
input_element.send_keys("17601" + Keys.ENTER)

# wait fot the new stores to load
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='set store']"))
)
# click the store I want to set
button = driver.find_element(By.CSS_SELECTOR, "[aria-label='set store']")
button.click()

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

# wait for new page to load
WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scct--image-gallery__image"))
        )

while find_all_cars(driver) == True:
    continue

# wait for new page to load
WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scct--image-gallery__image"))
        )

# start looping through the cars
buttons = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
car_info = [[]]
for index in range(len(buttons)):
    try:
        # Re-find the elements in case the page has changed
        elements = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
        element = elements[index]

        # Perform actions on each element - in this case, click on a car
        element.click()

        # -----------------------------------------------
        # GET ALL THE INFORMATION I WANT FROM A CARS PAGE
        array = get_car_facts(driver)
        car_info.append(array)
        print(array)
        # -----------------------------------------------

        # Optionally, wait for the page to load or perform other actions
        time.sleep(2)  # Add a delay if necessary
        driver.back()  # Go back to the previous page, if needed

    except Exception as e:
        print(f"Element at index {index} became stale.")
        continue  # Skip to the next iteration

file_path = 'output.csv'

# Write arrays to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(car_info)

driver.quit()