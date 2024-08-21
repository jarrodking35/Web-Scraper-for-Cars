from utils import *

first_run = True
buttons_len = 0

def find_all_cars(driver):
    '''
    This method is used to click the See More Matches button to pull up more cars. It waits for all
    of the new cars to load so that it can maintain an accurate count of the total cars available

    This method returns True if the button was able to be clicked, and it returns False if the button
    was never clicked
    '''
    global first_run, buttons_len

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

