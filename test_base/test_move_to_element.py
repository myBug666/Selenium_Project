'''
鼠标悬停
'''
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://127.0.0.1:8089/index.php')

ele = driver.find_element_by_link_text('手机、数码、通讯')
ActionChains(driver).move_to_element(ele).perform() # perform()-是链表的结束语句

driver.find_element_by_link_text('手机').click()
time.sleep(6)
driver.quit()

