from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# '''Lay duong dan'''
# driver = webdriver.Chrome(executable_path="D:/chromedriver.exe")
# driver.get("https:vnexpress.net/")
#
# print(driver.title)
#
# '''Lay cac bai dang'''
#
# acticles = driver.find_elements(By.CSS_SELECTOR, 'acticle.item-news')
# for a in acticles:
#     try:
#         title = a.find_element(By.TAG_NAME, 'h3').text
#         link = a.find_element(By.CSS_SELECTOR, 'h3.title-news>a'). get_attribute('href')
#         print(title)
#         print(link)
#     except NoSuchElementException:
#         print('Loi')
#
# driver.close()


'''duyet san pham tren trang thegioididong'''
'''Lay duong dan'''
driver = webdriver.Chrome(executable_path="D:\HK2-Năm3\KTPM\Chrome_driver\chromedriver.exe")
driver.get("https://www.thegioididong.com/")

print(driver.title)

'''Lay cac bai dang'''

products = driver.find_elements(By.CSS_SELECTOR, 'div.item')
for p in products:
    try:
        title = p.find_element(By.TAG_NAME, 'h3').text
        link = p.find_element(By.CSS_SELECTOR, 'a'). get_attribute('href')
        print(title)
        print(link)
    except NoSuchElementException:
        print('Loi')

driver.close()
