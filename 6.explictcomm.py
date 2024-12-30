from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

driver = webdriver.Chrome()

#mywait = WebDriverWait(driver,10) #explicit wait decleration #Basic
mywait = WebDriverWait(driver,10,ignored_exceptions=Exception)
#mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception)


driver.get('https://www.google.com/')
driver.maximize_window()

searchbox = driver.find_element(By.ID,"APjFqb") #searchbox is a variable

searchbox.send_keys('Selinium')
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.CLASS_NAME,'VuuXrf')))
searchlink.click()