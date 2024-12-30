from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

driver.switch_to.parent_frame()# here as there is only one parentframe and we want to acces the element of the parent class then we us this 

driver.switch_to.default_content()# it redirects the control to the browser as it exits from the frames

driver.find_element(By.XPATH,"//a[normalize-space()='WebTable']").click()

time.sleep(10)