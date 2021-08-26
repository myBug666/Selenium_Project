import time
from selenium import webdriver


#编写注册脚本
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10) # 隐式等待，只需上面写一次，下面遇到加载情况

# 1、打开浏览器  2、输入网址  3、输入用户名 4、输入密码 5、输入确认密码 6、输入手机号 7、输入E-mail 8、点击注册btn

driver.get('http://127.0.0.1:8089/index.php?m=user&c=public&a=reg')
time.sleep(1)
driver.find_element_by_name('username').click()
ActionChains(driver).send_keys('tjc123456').send_keys(Keys.TAB)\
    .send_keys('123456').send_keys(Keys.TAB)\
    .send_keys('123456').send_keys(Keys.TAB)\
    .send_keys('15112345678').send_keys(Keys.TAB)\
    .send_keys('tian123@qq.com').send_keys(Keys.TAB)\
    .send_keys(Keys.ENTER).perform()

# 表单形式才能使用链表形式操作



# driver.find_element_by_css_selector('.reg_btn').click()
# driver.find_element_by_class_name('reg_btn').click()
# driver.find_element_by_class_name('[value="注册"]').click()
# 9、关闭浏览器

# 提成脚本优化方面：
# 尽量少用强制等待
# 尽量用css_selector