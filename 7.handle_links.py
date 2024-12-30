from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window

#clicking on link
#driver.find_element(By.LINK_TEXT,"Apparel").click()

#finding the all links in the web app as all link has tagname we use that methos
links = driver.find_elements(By.TAG_NAME,'a')
#links = driver.find_elements(By.XPATH,"//a")
print(len(links))