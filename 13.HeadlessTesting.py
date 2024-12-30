from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def headless_chrome():
  ops = webdriver.ChromeOptions()
  ops.add_argument("--headless=new")#changeed in selenium 4.10.0
  driver = webdriver.Chrome(options=ops)
  return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
