import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe')

driver.get('http://127.0.0.1:8089/')

driver.maximize_window()  # 窗口最大化

driver.find_element_by_class_name('input_ss').send_keys('手机')

time.sleep(2)

driver.find_element_by_class_name('btn1').click()

time.sleep(3)

driver.quit()
