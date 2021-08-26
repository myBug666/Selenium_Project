import time
from selenium import webdriver

#编写注册脚本
# 1、打开浏览器
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10) # 隐式等待，只需上面写一次，下面遇到加载情况
# 2、输入网址
driver.get('http://127.0.0.1:8089/index.php?m=user&c=public&a=login')
# 3、输入用户名
time.sleep(1)
driver.find_element_by_css_selector('#username').clear() # 清除
driver.find_element_by_css_selector('#username').send_keys('tjc123456')
# driver.find_element_by_id('username').send_keys('tjc123456')
# 4、输入密码
time.sleep(1)
driver.find_element_by_css_selector('#password').clear() # 清除
driver.find_element_by_id('password').send_keys('123456')
# 5、点击登录btn
time.sleep(1)
# driver.find_element_by_class_name('login_btn').click()
# driver.find_element_by_css_selector('.login_btn')
driver.find_element_by_css_selector('[value="登　录"]').click()

time.sleep(3)

# 在后期优化脚本时，尽量使用隐式等待，取消强制等待
# WebDriverWait(driver,5,0.5).until(expected_conditions.title_contains)

# 1、登录成功以后，点击账号设置
driver.find_element_by_partial_link_text('账号设置').click()
# 2、点击个人资料
driver.find_element_by_partial_link_text('个人资料').click()
# 3.1、修改真实姓名
driver.find_element_by_css_selector('#true_name').clear()
driver.find_element_by_css_selector('#true_name').send_keys('张小龙')
# 3.2、修改性别
# 通过value定位
# driver.find_element_by_css_selector('[value="1"]').click()
# 通过id定位
driver.find_elements_by_css_selector('#xb')[1].click()
# 3.3、修改生日
# scrapy = 'document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(scrapy)

driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_css_selector('#date').clear()
driver.find_element_by_css_selector('#date').send_keys('2020-09-16')
# 3.4、修改QQ号
driver.find_element_by_css_selector('#qq').clear()
driver.find_element_by_css_selector('#qq').send_keys('1234567898')
# 3.5、点击确定
driver.find_element_by_css_selector('[value="确认"]').click()

# 4、点击弹框确定
time.sleep(2)
# driver.switch_to.alert.accept()  # 点击弹框确定
# driver.switch_to.alert.dismiss() # 点击弹框取消
text = driver.switch_to.alert.text   # 查看个人信息是否修改成功
print(text)
driver.switch_to.alert.accept()  # 点击弹框确定


# 关闭浏览器
time.sleep(8)
driver.quit()

# driver.find_element_by_partial_link_text('修改收货人姓名').click()
# driver.find_element_by_css_selector('#username').clear()
# driver.find_element_by_css_selector('#username').send_keys('田建朝')

# document.getElementById("date").removeAttribute("readonly")
