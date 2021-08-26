import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='D:chromedriver.exe')
# driver = webdriver.Ie()
# driver = webdriver.firefox
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(5) # 隐式等待，加载转圈等待、最多不超过5s

driver.get('http://www.baidu.com')

driver.find_element_by_id()
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_element_by_xpath()
driver.find_element_by_link_text() # a标签文本定位
driver.find_element_by_partial_link_text() # a标签部分定位
driver.find_element_by_tag_name() # 标签名定位
driver.find_element_by_css_selector() # css是层叠样式表、css_selector是层叠样式表选择器
                                      # 通过css方法定位id，在id元素前加#
                                      # 通过css方法定位class，在class元素前加.

# *****************************
ActionChains.move_to_element() # 鼠标悬停
ActionChains.double_click() # 鼠标双击
ActionChains.click_and_hold() # 鼠标点击到某一个元素上
ActionChains.context_click() # 鼠标右击
ActionChains.drag_and_drop() # 鼠标拖动
# *****************************

# perform()-是链表的结束语句
ActionChains(driver) # 链表--封装了全部的鼠标操作，使用Keys方法可以盗用大部分键盘操作
ActionChains(driver).double_click().perform() # Tab键  perform()-是链表的结束语句
ActionChains(driver).send_keys(Keys.TAB).perform() # Tab键
ActionChains(driver).move_to_element() # 鼠标悬停

# 跳转框架
driver.switch_to.frame('mainFrame')





