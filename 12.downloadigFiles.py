from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time




def chromium():
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome()
    return driver

def edge():
    from selenium.webdriver.edge.service import Service
    driver = webdriver.Edge()
    return driver

driver = edge()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.implicitly_wait(10)
try:
  # Locate the element using xpath
  browse_link = driver.find_element(By.LINK_TEXT, "Select file size & download")
  # Click the element if found
  browse_link.click()
  print("Clicked 'Browse' link successfully!")

except NoSuchElementException:
  print("Could not find the 'Browse' link on the page.")
# driver.find_element(By.XPATH,"//a[@href='https://file-examples.com/index.php/sample-documents-download/'][normalize-space()='Browse']").click()


time.sleep(10)