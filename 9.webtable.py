from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window

#1.counting number of rows and colums

row = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
# row = len(driver.find_element(By.XPATH,"//table[@name='BookTable']//tr"))

col = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))
# col = len(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

print(row,col)

#2.reading specific row and column data

data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[7]/td[3]").text
print(data)

#3.reading all rows and columns data
for r in range (2,row+1):
    for c in range(1,col+1):
        dataall = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text#passing number of row and column value dynamically
        print(dataall)
        print(dataall,end='               ')
    print()

#4 reading data based on conditions

for r in range(2,row+1):
    autname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if autname == "Amit":
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname, autname, price)

driver.close()