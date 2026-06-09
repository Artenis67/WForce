from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

chap1_svt_link = "https://view.genially.com/63075703bce35e001284f7dc"
driver = webdriver.Firefox()

driver.get(chap1_svt_link)

print("Driver Loading...")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

print("Driver Loaded !")

print("Veuillez vous rendre sur le champs sur lequel WF doit agir...")

input("Lancer WF ?")

input_elem = driver.find_element(By.CSS_SELECTOR, "input.Input-sc-4xpnwt.hryuwh[type='password']")
driver.execute_script("arguments[0].type = 'text';", input_elem)

input_elem.clear()
input_elem.send_keys("TEST")
input_elem.send_keys(Keys.RETURN)