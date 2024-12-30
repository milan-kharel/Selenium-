from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("")

#Capture cookies from the browser 
cookie = driver.get_cookies()
print(len(cookie))

#Print details of all cookies
for c in cookie:
    print(c)
    print(c.get('name'))
    print(c.get('value'),":",c.get('expiry'))

#aadding custom cookies
driver.add_cookie({"name":"Mycookie","value":"12345"})
cookie = driver.get_cookies()
print(len(cookie))

#deleting specific cookies from the browser
driver.delete_cookie("Mycookie")
cookie = driver.get_cookies()
print(len(cookie))

#deleting all the cookie
driver.delete_all_cookies()
cookie = driver.get_cookies()
print(len(cookie))


