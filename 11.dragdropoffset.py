from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()


driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.implicitly_wait(10)

min = driver.find_element(By.XPATH,"//span[1]")
maxi = driver.find_element(By.XPATH,"//span[2]")

print(min.location)
print(maxi.location)

act =ActionChains

    # draggable = driver.find_element(By.ID, "draggable")
    # start = draggable.location
    # finish = driver.find_element(By.ID, "droppable").location
    # ActionChains(driver)\
    #     .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y'])\
    #     .perform()


act.drag_and_drop_by_offset(driver, min, 69,  0).perform()





time.sleep(10)

