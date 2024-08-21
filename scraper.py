from utils import *
from car_facts import get_car_facts
from expand_search import find_all_cars
from set_store import store_setup
from set_distance import set_distance
from csv_formatter import output_format

def wait_for_loading(driver):
    '''
    This stalls the program until the tiles containing cars have loaded
    '''
    WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, "scct--image-gallery__image"))
            )
    return

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.carmax.com/cars/chevrolet/colorado")
# https://www.carmax.com/cars/toyota/tacoma
# https://www.carmax.com/cars/chevrolet/colorado

store_setup(driver)

# distance is set to 100 miles right now
set_distance(driver)

wait_for_loading(driver)

while find_all_cars(driver) == True:
    continue

wait_for_loading(driver)

# Loop through all the cars and get all information I need
buttons = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
car_info = [[]]
for index in range(len(buttons)):
    try:
        # Re-find the elements in case the page has changed
        elements = driver.find_elements(By.CLASS_NAME, "scct--image-gallery__image")
        element = elements[index]
        element.click()

        # -----------------------------------------------
        # GET ALL THE INFORMATION I WANT FROM A CARS PAGE
        array = get_car_facts(driver)
        car_info.append(array)
        # -----------------------------------------------

        # Optionally, wait for the page to load or perform other actions
        time.sleep(2)  # Add a delay if necessary
        driver.back()  # Go back to the previous page, if needed

    except Exception as e:
        print(f"Element at index {index} became stale.")
        continue  # Skip to the next iteration


output_format("colorado.csv", car_info)

driver.quit()