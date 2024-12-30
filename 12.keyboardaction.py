from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains, Keys

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")
driver = webdriver.Chrome(options=ops)


driver = webdriver.Chrome()


driver.get("https://text-compare.com/")
driver.implicitly_wait(20)

field1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("Hello I Am Here")

field2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

act = ActionChains(driver)

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(10)