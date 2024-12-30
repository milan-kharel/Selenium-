from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome()
driver.get("https://www.mheecha.com/mobile-home/")
driver.maximize_window

#using absolute xpath
#driver.find_element(By.XPATH,'/html/body/div[2]/div/header/div/div/div[1]/div/div/div[2]/div/div/form/div/input[1]').send_keys('bag')
#using relative xpath
#driver.find_element(By.XPATH,'//*[@id="searchsubmit"]').click()

#double quotation inside double quotation not allowed
#using or with xpath
#driver.find_element(By.XPATH,'//*[@id="s" or @name="s"]').send_keys('bag')
#using and with xpath
#driver.find_element(By.XPATH,'//*[@id="searchsubmit" and @value=""]').click()

#using contains() and startswith() if a element has dynamic function mostly this methods are used
driver.find_element(By.XPATH,'//input[contains(@id,"s")]').send_keys('bag')
driver.find_element(By.XPATH,'//input[starts-with(@id,"searchsubmit")]').click()

sleep(10)