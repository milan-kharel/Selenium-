from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.Google.com')

search_box = browser.find_element(By.NAME, 'q')
search_box.send_keys('seleniumhq' + Keys.RETURN)
sleep(10)

browser.quit()