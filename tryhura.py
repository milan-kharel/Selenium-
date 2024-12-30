from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://hurawatch.cc/")
driver.maximize_window

name = driver.find_element(By.XPATH,"//input[@placeholder='Search movies...']")
# mov = driver.find_element(By.XPATH,"//div[@class='body']//div[1]//a[1]']")

# act = ActionChains(driver)
# act.move_to_element(name).move_to_element(mov).click().perform()

time.sleep(10)