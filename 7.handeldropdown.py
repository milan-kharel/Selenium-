from selenium import webdriver
import requests as requests
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.opencart.com/index.php?route=account/register')

driver.find_element(By.XPATH,'//*[@id="input-username"]').send_keys("milann")


# driver.find_element(By.CSS_SELECTOR, "#input-country")
# email_field.send_keys("your_email@example.com")

# drpcountry = driver.find_element(By.XPATH,"//select[@id='input-country']")
# drp = Select(drpcountry)

# select_element = driver.find_element(By.NAME, 'country_id')
# select = Select(select_element)
# select.select_by_visible_text('Nepal')

#selecting option from dropdown
# drp.select_by_visible_text('Nepal')
# drp.select_by_value(30)
# drp.select_by_index(40)#index not shown manually on website we need to count it

#we can also directly select the element 
# drps = Select(driver.find_element(By.XPATH,"//*[@id='input-country']"))
# drps.select_by_visible_text('Nepal')
