from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
import os
import time


def nansen_request(website, contract):
    #variables
    EMAIL_ADDRESS = ""
    PWD = ""
    login_website = "https://pro.nansen.ai/auth/login"

    #open ChromeDriver to Nansen login page
    ChromeOptions = Options()
    ChromeOptions.add_argument("--window-size=1980,1020")
    ChromeOptions.add_argument("--headless")
    ChromeOptions.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ChromeOptions)
    driver.get(login_website)

    #enter email address on login page
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotSelectableException])
    delay = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    #email = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.NAME, "email"))
    email = driver.find_element(By.NAME, "email")
    email.send_keys(EMAIL_ADDRESS)

    #enter password on login page
    password = driver.find_element(By.NAME, "password")
    password.click()
    password.send_keys(PWD)

    #find Sign in button (The ID changes to prevent this kind of automation)
    buttons = driver.find_elements(By.TAG_NAME, "BUTTON")
    for b in buttons:
        if b.text == "Sign in":
            button = b

    #click Sign in button
    button.click()
    time.sleep(5)
    driver.get(website)

    # pause 5 second to let page loads
    time.sleep(5)

    #what if invalid contract or no data?
    url_title = driver.title
    #if url_title == "Nansen":
        #return None

    #Resizing webpage to get full screenshot
    ele = driver.find_element(by=By.TAG_NAME, value='html')
    total_height = ele.size["height"] + 800
    driver.set_window_size(ele.size["width"], total_height)

    # save screenshot
    driver.save_screenshot(contract + '.png')

    driver.close()
    driver.quit()

    return url_title