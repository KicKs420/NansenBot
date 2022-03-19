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

def nansen_request(website):
    #variables
    EMAIL_ADDRESS = ""
    PWD = ""
    #login_website = "https://pro.nansen.ai/auth/login"

    #open ChromeDriver with GoFullPage Extension
    chrome_options = Options()
    chrome_options.add_extension('extension_7_6_0_0.crx')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    #close GoFullPage Extension welcome window
    windows = driver.window_handles
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.close()

    #navigate to requested page (login required)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    driver.get(website)

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

    delay = wait.until(EC.element_to_be_clickable((By.ID, "nft_tgm_txs_breakdown")))
    #TransactionsandBuyers = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "nft_tgm_txs_breakdown"))

    #Trying to trigger the GoFullPage Chrome Extension via keyboard shortcut of ALT+SHIFT+P (not working)
    #webdriver.ActionChains(driver).key_down(Keys.ALT).send_keys("p").key_up(Keys.ALT).key_down(Keys.SHIFT).key_up(Keys.SHIFT).perform()

    #Resizing webpage to get full screenshot (not working)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot('screenshot.png')

    driver.close()
    driver.quit()



