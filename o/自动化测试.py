# selenium 是测试web
from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path='D:\chromedriver\chromedriver.exe')
# 设置等待时间
driver.implicitly_wait(3)

driver.get('http://www.51job.com')

# 查找需要的id 唯一标识
ele = driver.find_element_by_id('kwdselectid')

# 输入字符串
ele.send_keys('python')

time.sleep(1)

ele = driver.find_element_by_id('work_position_input')

time.sleep(1)

ele.click()

eles = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em[class=on]')

for ele in eles:
    ele.click()

driver.find_element_by_id(
    'work_position_click_center_right_list_category_000000_010000').click()

time.sleep(1)

driver.find_element_by_id('work_position_click_bottom_save').click()

time.sleep(1)

pass