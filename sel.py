from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
sleep(10)

browser.close()