from time import sleep  # Used to pause the program execution
from selenium import webdriver  # Used to automate browser interaction
from selenium.webdriver.common.by import By  # Used to locate elements on the web page
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get('http://www.Youtube.com')

# Find the search box on the page using its name attribute
search_box = browser.find_element(By.NAME, 'search_query')

# Type "seleniumhq" in the search box and press Enter
search_box.send_keys('new movie trailer') #use any keyword to search or browse the youtube
search_box.send_keys(Keys.RETURN)

sleep(30) 

browser.quit()
