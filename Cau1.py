from selenium import webdriver
from selenium.webdriver.common.by import By

'''Lay duong dan'''
driver = webdriver.Chrome(executable_path="D:\HK2-Năm3\KTPM\Chrome_driver\chromedriver.exe")
driver.get("https://www.google.com/")

str = input('Nhap tu khoa: ')

control = driver.find_element(By.NAME, 'q')
control.send_keys(str)
control.submit()

'''lay cac ket qua'''

results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
for re in results:
    text = re.find_element(By.TAG_NAME, 'a').text
    link = re.find_element(By.TAG_NAME, 'a').get_attribute('href')

    print(text)
    print(link)

driver.close()
