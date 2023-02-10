from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
driver = webdriver.Chrome()
driver.get("https://farmrpg.com/index.php#!/login.php")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('Leonhart')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('jt64agc2')

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_sub')))
login.click()

farm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'My Farm')]")))
farm.click()

# harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]")))
# harvest.click()

# plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All Selected')]")))
# plant.click()

while True:
    pass
