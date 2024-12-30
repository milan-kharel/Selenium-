from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")
driver = webdriver.Chrome(options=ops)


driver = webdriver.Chrome()


driver.get("https://www.browserstack.com/guide/selenium-scroll-tutorial")
driver.implicitly_wait(10)

#scrolling down by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print(value)

#scrolling till elements visible
# ele = driver.find_element(By.XPATH,"//a[normalize-space()='Try BrowserStack for Free']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# value = driver.execute_script("return window.pageYOffset;")
# print(value)

#scrolling till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)

time.sleep(5)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(value)


time.sleep(5)