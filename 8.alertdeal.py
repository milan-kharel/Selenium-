from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/basic_auth")

#authentication Method need ti inject password and username directly into popup or alert
driver.get("admin:admin@https://the-internet.herokuapp.com/basic_auth")
time.sleep(5)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(5)
# alertwin = driver.switch_to.alert
# print(alertwin.text)
# alertwin.send_keys("Welcome")# here we are using accept() method mean we are entering welcome then clicking OK button
# alertwin.dismiss()#we are closing the alert window with cancel button so the entered text is returned as NULL


