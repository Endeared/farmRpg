from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
  
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://farmrpg.com/index.php#!/login.php")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('Leonhart')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('jt64agc2')

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_sub'))).click()
time.sleep(0.5)
fishing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Go Fishing')]"))).click()
time.sleep(1)
driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
time.sleep(0.5)
fishing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Pirate')]"))).click()

# while True:
#     time.sleep(1)
#     fish = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fishcaught finalcatch1']"))).click()

