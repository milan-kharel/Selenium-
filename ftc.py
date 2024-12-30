from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()#driver is a object, chrome is a class getting accessed from webdriver module
#class cant be accessed directly so we need objects 
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button.oxd-button.orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else: print("Login Test Failed")

driver.close()