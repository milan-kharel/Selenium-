from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

# driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://www.mheecha.com/mobile-home/")
driver.implicitly_wait(10)

# driver.find_element(By.NAME, 'username').send_keys("Admin")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
prod = driver.find_element(By.XPATH,"//span[@class='menu-text'][normalize-space()='Products']")
backpack = driver.find_element(By.XPATH,"//span[@class='menu-text'][normalize-space()='Backpacks']")

act = ActionChains(driver)
act.move_to_element(prod).move_to_element(backpack).click().perform()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(10)

but = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)

act.context_click(but).perform()

# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

# outerframe = driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# driver.switch_to.frame(outerframe)

# fiel = driver.find_element(By.XPATH,"//input[@id='field1']")
# fiel.clear()
# fiel.send_keys("Bibek Daka")

# butt = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

# act = ActionChains(driver)

# act.double_click(butt).perform()

# drag and drop
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

# soele = driver.find_element(By.XPATH,"//div[@id='box1']")
# trele = driver.find_element(By.XPATH,"//div[@id='box101']")

# act = ActionChains(driver)

# act.drag_and_drop(soele,trele).perform()

time.sleep(10)