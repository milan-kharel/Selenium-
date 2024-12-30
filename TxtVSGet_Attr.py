from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

email = driver.find_element(By.ID,"Email")
print(email.get_attribute('value'))

email.clear()
email.send_keys("me@gmail.com")
print(email.get_attribute('value'))#returns value present in ID web element
print(email.text)#returns notthing as there is no innertext

email = driver.find_element(By.CLASS_NAME,"button-1")
print(email.text)#returns innertext