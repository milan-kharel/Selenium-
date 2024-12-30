from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.daraz.com.np/shop/mheecha/")

#find_element() - returns single web element

#1. locator matching with single webelement
# ele = driver.find_element(By.ID,"q")
# ele.send_keys("women")

#2. locator matching with multiple webelements
# ele = driver.find_element(By.XPATH,"//div[@class='footer-first']//a")
# print(ele.text)

#3 if element does not exist in we app then throw NoSuchElementException
# log = driver.find_element(By.LINK_TEXT,"Logi")
# log.click()

#find_elements( -returns multiple web elements)

#1. locator matching with single webelement
# ele = driver.find_elements(By.ID,"q")
# print(len(ele))
# ele[0].send_keys("women")

#2. locator matching with multiple webelements
# ele = driver.find_elements(By.XPATH,"//div[@class='footer-first']//a")
# print(len(ele))
# print(ele[0].text)
# for ele in ele:
#     print(ele.text)

#3 if elements does not exist in we get nothing
log = driver.find_elements(By.LINK_TEXT,"Logi")
print(len(log))
