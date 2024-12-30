from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from fourteen import XlUtil14

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/united-bank-of-india/fixed-deposit-calculator-UBO-BUB002.html?classic=true")
driver.maximize_window()

file="F:\selenium youtube\caldata.xls"

rows = XlUtil14.getRowCount()

for r in range (2,rows+1):
    #read data from xl
    pric = XlUtil14.readData(file,"Sheet1",r,1)
    ROI = XlUtil14.readData(file,"Sheet1",r,2)
    Period = XlUtil14.readData(file,"Sheet1",r,3)
    Freq = XlUtil14.readData(file,"Sheet1",r,4)
    exp_Matv = XlUtil14.readData(file,"Sheet1",r,5)
    #PASSING DATA INTO Application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(Period)

    #periodd = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    #periodd.select_by_visible_text(Period)

    #preqd= Select(driver.find_element(By.XPATH,"\\select[@id='frequency']"))
    #preqd.select_by_visible_text(Freq)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    clk = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(clk)==float(exp_Matv):
        print("test passed")
        XlUtil14.writeData(file,"Sheet1",r,8,"passed")
        XlUtil14.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XlUtil14.writeData(file,"Sheet1",r,8,"failed")
        XlUtil14.fillGreenColor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,"//*[@id='fdmatval']/div[2]/a[2]/img").click()
    time.sleep(2)

    driver.close()


    



    
    