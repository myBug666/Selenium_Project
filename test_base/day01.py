import time
# 导包快捷键alt+enter，在选择所需要的包

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='D:\chromedriver\chromedriver.exe')

driver.maximize_window()  # 窗口最大化
# driver.minimize_window()  # 空口最小化
# driver.set_window_size(480,900)  # 设置浏览器宽高
# driver.forward()  # 浏览器的前进
# driver.back()   # 浏览器的后退
# driver.refresh()  # 浏览器刷新
# driver.close()  # 关闭当前浏览器窗口（并非关闭超链接新打开的窗口）
# driver.quit()   # 退出浏览器

# 窗口切换
# 在Python中，选择最后一个可以用-1表示，获取最后一个窗口的句柄
# new_window = driver.window_handles[-1]

# # 获取第一个窗口的句柄
# old_window = driver.window_handles[0]
# # 通过浏览器句柄，切换到新的窗口 需要注意：switch_to方法
# driver.switch_to.window(new_window)

driver.switch_to.window(driver.window_handles[-1])

# driver.find_element_by_link_text() # a标签文本定位
# driver.find_element_by_id().send_keys() # 找到id，键入输入‘’


driver.get('http://www.baidu.com')

time.sleep(3)

driver.quit()

# 跳转
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.switch_to.window()
driver.switch_to.frame() # 框架

# 下拉框：Select   先确定是不是

pass
