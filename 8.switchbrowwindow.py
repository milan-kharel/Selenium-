from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(5)
windowid = driver.current_window_handle
print(windowid)

driver.find_element(By.LINK_TEXT,"YouTube").click()
windowids = driver.window_handles# returs list of multiple window id

parent = windowids[0]
node = windowids[1]
print(parent,node)

driver.switch_to.window(parent)
print(driver.title)

driver.switch_to.window(node)
print(driver.title)

#APPROACH 2 cause we might have multiples pages and creating the individual variable cos us space and efficency
for winid in windowids:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title == "nopCommerce demo store":
        driver.close()

time.sleep(10)