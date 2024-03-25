from time import sleep  # Used to pause the program execution
from selenium import webdriver  # Used to automate browser interaction
from selenium.webdriver.common.by import By  # Used to locate elements on the web page
from selenium.webdriver.common.keys import Keys  # Used to simulate keyboard interactions


browser = webdriver.Chrome()

browser.get('http://www.google.com')

# Find the search box on the page using its name attribute
search_box = browser.find_element(By.NAME, 'q')

# Type "seleniumhq" in the search box and press Enter
search_box.send_keys('seleniumhq' + Keys.RETURN)

sleep(10) 

browser.quit()
