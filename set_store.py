from utils import *

def store_setup(driver):
    '''
    This method goes through the process of setting the store location
    '''
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