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

fishing = True

while True:
    while fishing == True:
        try:
            fish = driver.find_element(By.CSS_SELECTOR, "img[src='/img/items/fish.png'][style*='display: inline']")
            fish.click()
            time.sleep(round(random.uniform(0.05, 0.12), 3))
            time.sleep(0.5)
            hook = driver.find_element(By.CSS_SELECTOR, "div[class*='fishcaught finalcatch']")
            hook.click()
            time.sleep(round(random.uniform(0.05, 0.12), 3))
        except:
            continue
        try:
            outOfWorms = driver.find_element(By.XPATH, "//strong[text()='0']")
        except:
            break
    
    time.sleep(0.5)
    sellAll = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button btngreenalt sellallfishbtnnc']"))).click()
    time.sleep(1)