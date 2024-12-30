from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
driver.implicitly_wait(5)

searchbox = driver.find_element(By.ID,"APjFqb") #searchbox is a variable

searchbox.send_keys('Selinium')
searchbox.submit()

# time.sleep(5)

driver.find_element(By.CLASS_NAME,'VuuXrf').click()

driver.quit()