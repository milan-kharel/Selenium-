from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")

# print(driver.title)#CAPTURE TITLE OF CURRENT PAGE
# print(driver.current_url)#CAPTURE CURRENT URL OF WEBPAGE
# print(driver.page_source)#CAPTURE SOURCE CODE OF PAGE

# driver.get("https://demo.nopcommerce.com/register")

# searchbox = driver.find_element(By.ID,"small-searchterms")
# print(searchbox.is_displayed())
# print(searchbox.is_enabled())

# #for radio buttons and checkbox Is Selected or not
# male = driver.find_element(By.ID,"gender-male")
# male.click()# selects the radio button else false is printed
# print(male.is_selected())

# female = driver.find_element(By.ID,"gender-female")
# print(female.is_selected())#false as we have not clicked the button

# driver.get("https://demo.nopcommerce.com/register")

# driver.find_element(By.LINK_TEXT,"nopCommerce").click()

# sleep(10)

#Navigational Command
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")

driver.back()#here browser goes back to snapdeal
driver.forward()# now again amazon is opened
driver.refresh()#here the page is refreshed



driver.quit()