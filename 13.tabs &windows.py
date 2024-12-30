from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("")
driver.maximize_window()
reglink = Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"").send_keys(reglink)

#opening a new tab and switching to it
driver.get("")
driver.switch_to.new_window('tab')
driver.get("")

#opening a new window and switching to it
driver.get("")
driver.switch_to.new_window('window')
driver.get("")



