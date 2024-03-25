# Import necessary libraries
from time import sleep  # Used to pause the program execution
from selenium import webdriver  # Used to automate browser interaction
from selenium.webdriver.common.by import By  # Used to locate elements on the web page
from selenium.webdriver.common.keys import Keys  # Used to simulate keyboard interactions

# Open a Chrome browser window
browser = webdriver.Chrome()

# Navigate to Google Search page
browser.get('http://www.google.com')  # Note: https://www.google.com is preferred for secure connection

# Find the search box on the page using its name attribute
search_box = browser.find_element(By.NAME, 'q')

# Type "seleniumhq" in the search box and press Enter
search_box.send_keys('seleniumhq' + Keys.RETURN)

# Simulate a short pause (optional, adjust as needed)
sleep(10)  # Pause for 10 seconds (consider using WebDriverWait for a more robust approach)

# Close the browser window
browser.quit()
