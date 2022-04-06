from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
'''Lay duong dan'''
driver = webdriver.Chrome(executable_path="D:\HK2-Năm3\KTPM\Chrome_driver\chromedriver.exe")
driver.get("https://www.facebook.com/")

#Doi 10s de tu dong nhap ket qua roi moi submit
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
driver.find_element(By.NAME,'firstname').send_keys('Hoc')
driver.find_element(By.NAME,'lastname').send_keys('Van')
driver.find_element(By.NAME,'reg_email__').send_keys('hoc1234@gamail.com')
driver.find_element(By.NAME,'reg_email_confirmation__').send_keys('hoc1234@gamail.com')
driver.find_element(By.NAME,'reg_passwd__').send_keys('a123B456!')

#31/3/2000
day = Select(driver.find_element(By.ID, 'day'))
day.select_by_visible_text('31')
month = Select(driver.find_element(By.ID, 'month'))
month.select_by_visible_text('Mar')
year = Select(driver.find_element(By.ID, 'year'))
year.select_by_visible_text('2000')

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.NAME, "websubmit").click()

driver.close()
