from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#self
#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/self::a").text
#print(text_msg)

#parent
#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/parent::td").text
#print(text_msg)

#child
#childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/child::td")
#print(len(childs))

#ancestor
#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr").text
#print(text_msg)

#decedent
#text_msg = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/descendant::*")
#print(len(text_msg))

#f0ll0wing
#followings = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/following::*")
#print(len(followings))

#following sibling
# followingsib = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/following-sibling::tr")
# print(len(followingsib))

#preceding
# prec = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/preceding::*")
# print(len(prec))

#preceding-sibling
prec = driver.find_elements(By.XPATH,"//a[contains(text(),'Hindustan Aeronautic')]/ancestor::tr/preceding-sibling::tr")
print(len(prec))

sleep(10)