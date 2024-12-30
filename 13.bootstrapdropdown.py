from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")


for countrylist in country:
    if countrylist.text=="Nepal":
        countrylist.click()
        break

print(len(country))

driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()




