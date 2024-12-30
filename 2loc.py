from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service

#serv_obj=Service("your chrome location in pc")
driver = webdriver.Chrome()

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window() # to maximize the browser window

#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo")
#driver.find_element(By.NAME,"q").send_keys("Lenovo")

#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()

# driver.get("https://www.mheecha.com/mobile-home/")

# sliders=driver.find_elements(By.CLASS_NAME,'qode_category_showcase_product_info_holder_inner')
# print(len(sliders))

# links=driver.find_elements(By.TAG_NAME,'a')
# print(len(links))

driver.get("https://www.facebook.com/")

#tag and id{Syntax: "tagname#valueofid"}
#driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('melon')
#driver.find_element(By.CSS_SELECTOR,'#email').send_keys('melon')

#tag and Class{Syntax: "tagname.valueofclass"}
#driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('melon')
#driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('melon')

#tag and Attribute{Syntax: "tagname[attribute=value]"}
#driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys('melon')
#driver.find_element(By.CSS_SELECTOR,'[data-testid=royal_email]').send_keys('melon')

#tag, class and attribute{Syntax: "tagname.valueofclass[attribute=value]"}


driver.quit()