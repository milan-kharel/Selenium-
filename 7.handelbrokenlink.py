from selenium import webdriver
import requests as requests
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')

links = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," is broken links")
        count+= 1
    else:
        print(url," is valid link")

print("total no of invalid link is:",count)

