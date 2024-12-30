from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")# it is neither disabling nor accepting the notification rather it is disabling the popup

driver = webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/#google_vignette")
driver.maximize_window

time.sleep(10)