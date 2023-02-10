from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
driver = webdriver.Chrome()
driver.get("https://farmrpg.com/index.php#!/login.php")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('Leonhart')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('jt64agc2')

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_sub'))).click()

farm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'My Farm')]"))).click()


time.sleep(5)
harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
time.sleep(5)
plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()
time.sleep(1)


driver.get("https://farmrpg.com/#!/store.php")
time.sleep(3)
max = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='maxqty cmaxbtn'][@data-id='14'][contains(text(), '+MAX')]"))).click()
time.sleep(1)
buy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='price14']"))).click()
time.sleep(5)
buy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='actions-modal-button'][contains(text(), 'Yes')]"))).click()
time.sleep(3)
ok = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='modal-button'][contains(text(), 'OK')]"))).click()
time.sleep(1)

back = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Back')]"))).click()
time.sleep(3)
temple = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Temple of Reward')]"))).click()
time.sleep(3)

eggplant = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@style='font-size:11px'][contains(text(), 'Sacrifice: Eggplant')]"))).click()
time.sleep(3)
sacrifice = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button sacrificebtn'][contains(text(), 'GO')]"))).click()
time.sleep(3)
buy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='actions-modal-button'][contains(text(), 'Yes')]"))).click()
time.sleep(3)
ok = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='modal-button modal-button-bold'][contains(text(), 'OK')]"))).click()
time.sleep(1)





harvesting = True
while harvesting == True:
    time.sleep(65)

    harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
    time.sleep(5)
    plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()

while True:
    pass
