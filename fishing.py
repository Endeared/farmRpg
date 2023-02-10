from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
  
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://farmrpg.com/index.php#!/login.php")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('Leonhart')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('jt64agc2')

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_sub'))).click()
time.sleep(0.5)
fishing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Go Fishing')]"))).click()
time.sleep(0.5)
# fishing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Pirate')]"))).click()
driver.get('https://farmrpg.com/#!/fishing.php?id=11')

while True:
    hooked = False
    while hooked == False:
        try:
            fish = driver.find_element(By.CSS_SELECTOR, "img[src='/img/items/fish.png'][style*='display: inline']")
            if bool(fish) == True:
                time.sleep(round(random.uniform(0.1, 0.2), 3))
                fish.click()
                try:
                    hook = driver.find_element(By.XPATH, "//div[@class='fishcaught finalcatch1']")
                    if bool(hook) == True:
                        hooked = True
                        break
                except:
                    continue
        except:
            continue
    while hooked == True:
        try:
            hook = driver.find_element(By.XPATH, "//div[@class='fishcaught finalcatch1']")
            if bool(hook) == True:
                time.sleep(round(random.uniform(0.1, 0.2), 3))
                hook.click()
                try:
                    hook = driver.find_element(By.XPATH, "//div[@class='fishcaught finalcatch1']")
                    if bool(hook) == False:
                        hooked = False
                        break
                except:
                    continue
            elif bool(hook) == False:
                hooked = False
                break
        except:
            continue
