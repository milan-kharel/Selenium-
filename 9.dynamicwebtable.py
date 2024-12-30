from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be present and interactable
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys("Admin")
    
    # Wait for the password field and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_field.send_keys("admin123")
    
    # Wait for the submit button and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    admin_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Admin'))
    )
    admin_field.click()

    



    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

