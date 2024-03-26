from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.implicitly_wait(10)

browser.get('https://www.instagram.com/')

username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

username_input.send_keys("your_username")
password_input.send_keys("your_password")

login_button = browser.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()

sleep(10)

browser.close()