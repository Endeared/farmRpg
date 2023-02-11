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
farm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'My Farm')]"))).click()
time.sleep(2)
harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
time.sleep(2)
plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()
time.sleep(1)

while True:
    for i in range(0, 30):
        time.sleep(305)
        harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
        time.sleep(2)
        plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()

    harvesting = True

    while harvesting == True:
        time.sleep(1)
        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Home')]"))).click()
        time.sleep(2)
        town = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Go into Town')]"))).click()
        time.sleep(2)
        store = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Country Store')]"))).click()
        time.sleep(2)
        max = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='maxqty cmaxbtn'][@data-id='12'][contains(text(), '+MAX')]"))).click()
        time.sleep(1)
        buy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='price12']"))).click()
        time.sleep(1)
        buy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='actions-modal-button'][contains(text(), 'Yes')]"))).click()
        time.sleep(1)
        ok = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='modal-button'][contains(text(), 'OK')]"))).click()
        time.sleep(1)

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Home')]"))).click()
        time.sleep(2)
        town = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Go into Town')]"))).click()
        time.sleep(2)
        market = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Farmer')]"))).click()
        time.sleep(2)
        sellUnlocked = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sell Unlocked')]"))).click()
        time.sleep(1)
        yes = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='actions-modal-button'][contains(text(), 'Yes')]"))).click()
        time.sleep(1)
        ok = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='modal-button modal-button-bold'][contains(text(), 'OK')]"))).click()
        time.sleep(1)

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-title'][contains(text(), 'Home')]"))).click()
        time.sleep(2)
        farm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'My Farm')]"))).click()
        time.sleep(2)

        for i in range(0, 30):
            if i == 0:
                time.sleep(280)
                harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
                time.sleep(2)
                plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()
                print(i)
            else:
                time.sleep(305)
                harvest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Harvest All')]"))).click()
                time.sleep(2)
                plant = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Plant All')]"))).click()
                print(i)

while True:
    pass
