from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window

driver.switch_to.frame(0)

#mm/dd/yyyy

driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/22/2020")

#logic to select date and day if sometime the sendkeys action doesnot work

month = "September"
year = "1999"
date = "23"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[1]").text
    yr = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[2]").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        #above we are clicking previous button but if we want a date to be selected in future then we need to click forward button elements

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

time.sleep(10)