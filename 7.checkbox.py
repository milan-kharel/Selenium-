from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)

#selecting specific checkbox
# checkboxes = driver.find_element(By.XPATH,"//*[@id='sunday']")
# checkboxes.click()

#sleep(10)

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains (@id,'day')]")
# print(len(checkboxes))

#approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#approach 2
for checkbox in checkboxes:
    checkbox.click()

#approach 3 to click whichever only we want to select
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

#approach 4 to select last two elements
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#approach 5 to select first two checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#approach 6 to clear all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()