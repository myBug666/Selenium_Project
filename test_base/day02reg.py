import time
from selenium import webdriver

#编写注册脚本
# 1、打开浏览器
driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10) # 隐式等待，只需上面写一次，下面遇到加载情况
# 2、输入网址
driver.get('http://127.0.0.1:8089/index.php?m=user&c=public&a=reg')
# 3、输入用户名
time.sleep(2)
driver.find_element_by_name('username').send_keys('tjc123456')
# 4、输入密码
time.sleep(2)
driver.find_element_by_name('password').send_keys('123456')
# 5、输入确认密码
time.sleep(2)
driver.find_element_by_name('userpassword2').send_keys('123456')
# 6、输入手机号
time.sleep(2)
driver.find_element_by_name('mobile_phone').send_keys('13512345679')
# 7、输入E-mail
time.sleep(2)
driver.find_element_by_name('email').send_keys('123456@qq.com')
# 8、点击注册btn
time.sleep(2)
driver.find_element_by_css_selector('.reg_btn').click()
# driver.find_element_by_css_selector('.reg_btn').submit() # 是表单的才可以提交
# driver.find_element_by_class_name('reg_btn').click()
# driver.find_element_by_class_name('[value="注册"]').click()
# 9、关闭浏览器
time.sleep(2)
driver.quit()

# 提成脚本：
# 尽量少用强制等待
# 尽量用css_selector